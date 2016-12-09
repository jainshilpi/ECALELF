#!/bin/bash
bold=$(tput bold)
normal=$(tput sgr0)

function testStep(){
	stepIndex=$1
	stepString=$2
	stepLog=$3
	stepCommand=$4
	
	dir=tmp/releaseValidation/$stepIndex
	if [ ! -d "$dir" ];then mkdir $dir; fi

	if [ -e "$dir/done" ]; then
		echo  "[`basename $0`] $stepString OK "
		return 0
	fi
	if [ ! -e "$dir/$stepLog.log" ];then
		echo -n "[`basename $0`] $stepString ... "
		cd $dir
		$stepCommand &> $stepLog.err || {
			echo "${bold}ERROR${normal}"
			echo "See $dir/$stepLog.err"
			exit 1
		}
		cd -
		mv $dir/$stepLog.{err,log}
		echo "OK"
	else
		echo "[`basename $0`] $stepString already done and OK"
	fi
	return 1
}
	
############################################################
# script to make sure that the new release is not breaking things
############################################################

echo "[`basename $0`] CMSSW RELEASE: $CMSSW_VERSION"
if [ ! -d "tmp/releaseValidation" ];then mkdir tmp/releaseValidation -p; fi

case $CMSSW_VERSION in
	CMSSW_8_0_*)
		fileMINIAOD=/store/mc/RunIISpring16MiniAODv1/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/00000/008099CA-5501-E611-9AAE-24BE05BDCEF1.root
		fileMINIAODData=/store/data/Run2016H/DoubleEG/MINIAOD/PromptReco-v3/000/284/036/00000/1878DF24-619F-E611-A962-02163E0146C8.root
		fileALCARAWData=/store/data/Run2016H/DoubleEG/ALCARECO/EcalUncalZElectron-PromptReco-v3/000/284/036/00000/240108A1-599F-E611-A3A5-FA163E7F2F56.root
		;;
	*)
		echo "CMSSW RELEASE not supported" >> /dev/stderr
		exit 1
		;;
esac


############################################################
# production in local of ntuples from MINIAOD
logName=ntuple_miniaodsim_mc
testStep 1 "Testing local production of ntuples from MINIAODSIM (MC)" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/80X_mcRun2_asymptotic_2016_miniAODv2.py type=MINIAODNTUPLE maxEvents=-1 doTree=1 doEleIDTree=1 files=$fileMINIAOD outputAll=True" || {

	python test/dumpNtuple.py $dir/ 1> $dir/$logName.dump 2> $dir/${logName}_2.log || {
		echo "${bold}ERROR${normal}"
		echo "See $dir/${logName}_2.log" 
		exit 1
	}

	echo -n "[`basename $0`] Checking difference in dump of ntuple content ... "
	diff -q {$dir,test}/${logName}.dump > /dev/null || {
		echo "${bold}ERROR${normal}"
		echo "{$dir,test}/${logName}.dump are different" 
		echo "you can use"
		echo "wdiff -n {$dir,test}/${logName}.dump | colordiff  | less -RS"
		exit 1
	}
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}


################
logName=ntuple_miniaodsim_data
testStep 2 "Testing local production of ntuples from MINIAODSIM (DATA)" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/80X_dataRun2_Prompt_v14.py type=MINIAODNTUPLE maxEvents=-1 doTree=1 doEleIDTree=1 files=$fileMINIAODData outputAll=True  isCrab=1" || {
	
	python test/dumpNtuple.py $dir/ 1> $dir/$logName.dump 2> $dir/${logName}_2.log || {
		echo "${bold}ERROR${normal}"
		echo "See $dir/${logName}_2.log" 
		exit 1
	}

	echo -n "[`basename $0`] Checking difference in dump of ntuple content ... "
	diff -q {$dir,test}/${logName}.dump > /dev/null || {
		echo "${bold}ERROR${normal}"
		echo "{$dir,test}/${logName}.dump are different" 
		echo "you can use"
		echo "wdiff -n {$dir,test}/${logName}.dump | colordiff  | less -RS"
		exit 1
	}
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}


################
logName=alcarereco_data
testStep 3 "Testing local production of alcarereco from DATA" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/80X_dataRun2_Prompt_v14.py type=ALCARERECO maxEvents=500 doTree=0 doEleIDTree=0 files=$fileALCARAWData outputAll=True  isCrab=1" || {
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}

################
logName=ntuple_alcarereco_data
testStep 4 "Testing local production of ntuples from alcarereco (DATA)" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/80X_dataRun2_Prompt_v14.py type=ALCARERECO maxEvents=-1 doTree=1 doEleIDTree=1 doTreeOnly=1 files=file:$PWD/$dir/EcalRecalElectron.root outputAll=True  isCrab=1" || {

	python test/dumpNtuple.py $dir/ 1> $dir/$logName.dump 2> $dir/${logName}_2.log || {
		echo "${bold}ERROR${normal}"
		echo "See $dir/${logName}_2.log" 
		exit 1
	}

	echo -n "[`basename $0`] Checking difference in dump of ntuple content ... "
	diff -q {$dir,test}/${logName}.dump > /dev/null || {
		echo "${bold}ERROR${normal}"
		echo "{$dir,test}/${logName}.dump are different" 
		echo "you can use"
		echo "wdiff -n {$dir,test}/${logName}.dump | colordiff  | less -RS"
		exit 1
	}
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}

################
logName=alcarereco_data
testStep 5 "Testing local production of ntuples from alcarereco (DATA)" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/Cal_Nov2016_ped_v1.py type=ALCARERECO maxEvents=-1 doTree=0 doEleIDTree=0 doTreeOnly=0 files=$fileALCARAWData outputAll=True  isCrab=1" || {
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}


################
logName=ntuple_alcarereco_data
testStep 6 "Testing local production of ntuples from alcarereco (DATA)" $logName "cmsRun $PWD/python/alcaSkimming.py tagFile=$PWD/config/reRecoTags/Cal_Nov2016_ped_v1.py type=ALCARERECO maxEvents=-1 doTree=1 doEleIDTree=1 doTreeOnly=1 files=file:$PWD/$dir/EcalRecalElectron.root outputAll=True  isCrab=1" || {

	python test/dumpNtuple.py $dir/ 1> $dir/$logName.dump 2> $dir/${logName}_2.log || {
		echo "${bold}ERROR${normal}"
		echo "See $dir/${logName}_2.log" 
		exit 1
	}

	echo -n "[`basename $0`] Checking difference in dump of ntuple content ... "
	diff -q {$dir,test}/${logName}.dump > /dev/null || {
		echo "${bold}ERROR${normal}"
		echo "{$dir,test}/${logName}.dump are different" 
		echo "you can use"
		echo "wdiff -n {$dir,test}/${logName}.dump | colordiff  | less -RS"
		exit 1
	}
	echo "OK"
	touch $dir/done
#	rm $dir/*.root
}





exit 0


