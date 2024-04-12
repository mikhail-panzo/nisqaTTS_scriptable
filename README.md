# Sample Python function
    from nisqaceb.NISQA_model import nisqaModel

    def check_quality(wav_file):
        args = {
            'mode': 'predict_file', 
            'pretrained_model': 'weights/nisqa.tar',
            'deg': wav_file,
            'data_dir': None,
            'output_dir': 'results',
            'csv_file': None,
            'csv_deg': None,
            'num_workers': 0,
            'bs': 1,
            'ms_channel':None,
            'tr_bs_val': 1,
            'tr_num_workers': 0
        }
    
        nisqa = nisqaModel(args)
        results = nisqa.predict()
        return results
