from recbole.quick_start import run_recbole

parameter_dict = {
   'neg_sampling': None,
}
run_recbole(model='BERT4Rec', dataset='ml-100k', config_dict=parameter_dict)
