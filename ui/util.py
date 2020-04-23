from .smpl.smpl_webuser.serialization import load_model as load_smpl_model
from .smpl.smpl_webuser.serialization import load_smplx_model, load_flame_model

base_model_folder = 'E:/DataSets/human_models/'

smpl_male_model_path = base_model_folder + 'smpl/basicmodel_m_lbs_10_207_0_v1.0.0.pkl'
smpl_female_model_path = base_model_folder + 'smpl/basicModel_f_lbs_10_207_0_v1.0.0.pkl'

smplx_male_model_path = base_model_folder + 'smplx/SMPLX_MALE.pkl'
smplx_female_model_path = base_model_folder + 'smplx/SMPLX_FEMALE.pkl'

flame_male_model_path = base_model_folder + 'flame/male_model.pkl'
flame_female_model_path = base_model_folder + 'flame/female_model.pkl'

def load_model(model_type='smplx',gender='m'):
	if model_type=='smplx':
		if gender=='m':
			return load_smplx_model(smplx_male_model_path)
		else:
		    return load_smplx_model(smplx_female_model_path)
	elif model_type=='smpl':
		if gender=='m':
			return load_smpl_model(smpl_male_model_path)
		else:
			return load_smpl_model(smpl_female_model_path)
	elif model_type=='flame':
		if gender=='m':
			return load_flame_model(flame_male_model_path)
		else:
			return load_flame_model(flame_female_model_path)