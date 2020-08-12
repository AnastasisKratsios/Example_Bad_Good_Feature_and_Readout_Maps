# This file contains the hyper-parameter grids used to train the imprinted-tree nets.

# Training Parameters
#----------------------#
# Number of Jobs (Cores to use)
n_jobs = 2
# Number of Random CV Draws
n_iter = 1
n_iter_trees = 1#20
# Number of CV Folds
CV_folds = 2#

#----------------------#
########################
# Hyperparameter Grids #
########################
#----------------------#

Random_Depths_Readout = 10
Random_Depths = np.array([2])#, 100, 500])#, 3,10, 20, 50, 100, 150,200, 500])
N_Features = 1# Random_Depths.shape[0]
N_Features_Search_Space_Dimension = 10**4


# Hyperparameter Grid (Readout)
#------------------------------#
param_grid_Vanilla_Nets = {'batch_size': [32],
                    'epochs': [2],#00, 400, 800, 1000, 1200, 1600],
                      'learning_rate': [0.0001],#,0.0005,0.005],
                      'height': [200],#, 400, 800, 1000],
                       'depth': [2],#, 4, 6],
                      'input_dim':[10],
                       'output_dim':[1]}

param_grid_Nice_Nets = {'batch_size': [32],#, 64],
                    'epochs': [200],#, 400, 800, 1000, 1200, 1600],
                      'learning_rate': [0.0001],#,0.0005,0.005],
                      'height': [100],#[50, 200, 400, 800, 1000],
                        'Depth_Feature_Map': [4],
                        'Depth_Readout_Map': [4],
                      'input_dim':[10],
                       'output_dim':[1]}

                       
# Random Forest Grid
#--------------------#
Rand_Forest_Grid = {'learning_rate': [0.1],#, 0.05, 0.02, 0.01, 0.01],
                    'max_depth': [4],#, 6, 10,50, 100],
                    'min_samples_leaf': [3],#, 5, 9, 17, 50, 100, 150, 200],
                   'n_estimators': [1],#00, 200, 500, 1000]
                   }