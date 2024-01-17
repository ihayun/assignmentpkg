import pytest
import Analysis

def test_analysis_load_data():
    analysis_obj = Analysis('analysis_config.yml')
    analysis_obj.load_data()
    
    assert analysis_obj.data != {}

def test_analysis_output():
    analysis_obj = Analysis('analysis_config.yml')
    analysis_obj.load_data()
    analysis_obj.compute_analysis()

    for output in analysis_obj.analysis_output:
        assert analysis_obj.analysis_output[output] != -1

