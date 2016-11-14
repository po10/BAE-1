import ROOT as r
from workflow import workflow

f = r.TFile("../tuples/bae-mc-11114003-2012-down.root")
t = f.Get("bar-muon-tuple/DecayTree")

fnew = r.TFile("newtree.root","RECREATE")
tnew = t.CloneTree(-1,'fast')
tnew.SetBranchStatus('*',0)



myworkflow = workflow()

myworkflow.module_names.append('addRestFrameVars')


myworkflow.run(tnew)

fnew.cd()
tnew.Write()
fnew.Close()
