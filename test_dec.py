from SigProfilerExtractor import decomposition as decomp

def main():
    #data = sig.importdata("text")
    signatures = "Results_scenarios/output_scenario_newsigtest_11/SBS96/All_Solutions/SBS96_3_Signatures/Signatures/SBS96_S3_Signatures.txt"
    activities="Results_scenarios/output_scenario_newsigtest_11/SBS96/All_Solutions/SBS96_3_Signatures/Activities/SBS96_S3_NMF_Activities.txt"
    samples="Synthetic_scenarios/Scenario1-14/scenario_11/Samples.txt"
    output="output_decompose_test_custom/"
    signature_dats="COSMIC_v3.2_SBS_GRCh38_test.txt"

    decomp.decompose(signatures, activities, samples, output, genome_build="GRCh37", verbose=False,signature_database=signature_dats)

if __name__ == '__main__':
    main()