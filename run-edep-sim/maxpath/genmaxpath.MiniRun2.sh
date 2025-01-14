#!/usr/bin/env bash

# run me from run-edep-sim

export ARCUBE_CONTAINER=mjkramer/sim2x2:genie_edep.LFG_testing.20230228
tune=D22_22a_02_11b

./GENIE_max_path_length_gen.sh geometry/Merged2x2MINERvA_v2/Merged2x2MINERvA_v2_withRock.gdml $tune
./GENIE_max_path_length_gen.sh geometry/Merged2x2MINERvA_v2/Merged2x2MINERvA_v2_noRock.gdml $tune
./GENIE_max_path_length_gen.sh geometry/Merged2x2MINERvA_v2/Merged2x2MINERvA_v2_justRock.gdml $tune
