#!/usr/bin/env bash
# vim ft=bash

# set -o xtrace # Enable for debuggin

[[ -f "utils" ]] && . utils

#################
# START CONS DEF
#################

ENVIRONMENT="dev"
DOCKER_SERVICE_CODE="dev"
OVERWRITE=""
DOCKER_SERVICE="$DOCKER_SERVICE_CODE"

###############
# END CONS DEF
###############

export VAR_UID=$(id -u)

_select_docker_service (){
        case $1 in
          code ) DOCKER_SERVICE="$DOCKER_SERVICE_CODE";;
        esac
}

_select_overwrite () {
        case $1 in 
          gpu ) OVERWRITE="-f docker-compose.yaml -f $OVERWRITE_GPU";; # Define docker compose overides
        esac
}

_load_buildargs () {
  # Loads build args from the file in $1
  # if they are prefixed with BUILD_
  env_files=$(grep -A 1 env_file docker-compose.yaml | grep / | cut -d"-" -f2)
  for file in $env_files; do
  for arg in $(cat $file); do
        suffix=$(echo $arg | cut -d"_" -f2-)
        [[ $arg =~ ^BUILD* ]] && declare -g -x $suffix 
    done
  done
}

_docker_compose () {
  _load_buildargs
  docker-compose $OVERWRITE --profile $ENVIRONMENT $@
}

_compose_run () {
        echo "$1"
       _docker_compose run $DOCKER_SERVICE $@
}



die() { echo "$*" >&2; exit 2; }  # complain to STDERR and exit with error
needs_arg() { if [ -z "$OPTARG" ]; then die "No arg for --$OPT option"; fi; }

while getopts o:s:-:p OPT; do
  # support long options: https://stackoverflow.com/a/28466267/519360
  if [ "$OPT" = "-" ]; then   # long option: reformulate OPT and OPTARG
    OPT="${OPTARG%%=*}"       # extract long option name
    OPTARG="${OPTARG#$OPT}"   # extract long option argument (may be empty)
    OPTARG="${OPTARG#=}"      # if long option argument, remove assigning `=`
  fi
  ## Here we add all the options
  case "$OPT" in
    o | overwrite ) needs_arg; _select_overwrite "$OPTARG";;
    p | prod )     ENVIRONMENT="prod";;
    s | service )  needs_arg;  _select_docker_service "$OPTARG";;
    ??* )          die "Illegal option --$OPT" ;;  # bad long option
    ? )            exit 2 ;;  # bad short option (error reported via getopts)
  esac
done

shift $((OPTIND-1)) # remove parsed options and args from $@ list
# command="$@" # What remains is the positional command

command=$( echo $@ | cut -d" " -f 1)
params=$( echo $@ | cut -d" " -f2-)

case $command in
        dc  ) _docker_compose "$params";; # generic docker compose
        run ) _compose_run "$params";; # run general commands in compose
        utils ) _compose_run "${!params}";; # run a command defined in utils
        *) die "Illegal command --$command";; # bad command
esac
