import os,sys
os.chdir(sys.path[0])
scen_name = "8"
inputfile = 'Synthetic_scenarios/Scenario1-14/' + 'scenario_' + str(scen_name)+'/'+'Samples.txt' 
outputdir = 'Results_scenarios/output_scenario_'+str(scen_name)
 
from SigProfilerExtractor import sigpro as sig
 
def run():
    #sig.sigProfilerExtractor('matrix',outputdir,inputfile,nmf_replicates=100,opportunity_genome='GRCh37',cosmic_version=3.2,collapse_to_SBS96=True,minimum_signatures=1,maximum_signatures=30,context_type="default",precision= "single",nmf_init="random",precision= "single",matrix_normalization= "gmm",seeds= "none",min_nmf_iterations= 5000,max_nmf_iterations=10000,nmf_test_conv= 1000,nmf_tolerance= 1e-7,gpu=False,cpu=28)
    sig.sigProfilerExtractor('matrix',
    outputdir,
    inputfile,
    nmf_replicates=100,
    opportunity_genome='GRCh37',
    cosmic_version=3.2,
    collapse_to_SBS96=True,
    minimum_signatures=1,
    maximum_signatures=6,
    context_type="default",
    gpu=False,
    precision = 'single',
    nmf_init= 'random',
    # min_nmf_iterations= 10000,
    # max_nmf_iterations=10000,
    # nmf_test_conv= 1,
    # nmf_tolerance= 1e-7,
    #nmf_init='clustering',
    cpu=8)
 
if __name__ == '__main__':
    run()