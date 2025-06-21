# HSDT Testing
This repo has all the required files for testing the [HSDT](https://github.com/Zeqiang-Lai/HSDT),
as well as its companion tester [HSIR](https://github.com/bit-isp/HSIR/)

The HSDT files are inside the hsdt folder
From HSIR, only the required folders of /hsir and /hsirun are copied.

## Steps to run 
1. Download the mat files from this [link](https://www.ehu.eus/ccwintco/index.php?title=Hyperspectral_Remote_Sensing_Scenes#Indian_Pines) into the `data/raw` folder
For testing purposes, I downloaded
- Indian_pines.mat
- Pavia.mat
- PaviaU.mat
- Salinas.mat

2. Run the `main.py` from the `src` folder in order to process the files.
```
cd src
python -m main
```


3. Run the following code to test and benchmark HSDT.
```
python -m hsirun.test -a hsdt.hsdt.hsdt -r models/hsdt_m_complex.pth -kp "" -d data -t noise_gaussian_30
```

Explanation: 
- `python -m hsirun.test` Run the `/hsirun/test.py` file.
Note that we are not running the hsir from its remote package since I had to make a small change.
- `-a hsdt.hsdt.hsdt` Set the 'arch' parameter as the hsdt model from `hsdt/hsdt/arch.py`
- `-r models/hsdt_m_complex.pth` 
Set the 'resume' parameter which is a parameter for the checkpoint.
Ensure it is set to one of the .pth models from `models/`
- `-kp ""`   
Set the 'key_path' parameter which is the 'key' meant to identify the checkpoint inside the .pth files.  
For whatever reason, it seems like the .pth files from HSDT have their checkpoint in the root;
not inside a specific key.   
This cannot be done in the original code. This is only possible due to changes made to the HSIR codebase.
- `-d data` Set the 'basedir' parameter to the data folder.
- `-t noise_gaussian_30` Set the 'testset' parameter to the noise folder containing the mat files.
Note that the basedir and testset parameter are joined together in the testing code as `data/noise_gaussian_30`   
You can also try testing `data/noise_gaussian_50` and `data/noise_gaussian_70`  

Note that the `hsdt_s_complex.pth` and `hsdt_l_complex.pth` does not seem to working due to the wrong shape. 

3b. If you want to record the error logs given from the command, run the following command instead
```
python -m hsirun.test -a hsdt.hsdt.hsdt -r models/hsdt_m_gaussian.pth -kp "" -t noise_gaussian_30 > logs/hsdt_test.log 2>&1
```
This will record the error logs in `logs/hsdt_test.log` file.

## Changes made to original code
In `/hsirun/test.py`, the following code around line-124 to line-131 is the edited one.   

```python
if args.key_path and args.key_path.strip():
    ckpt = tl.utils.dict_get(state, args.key_path)
    if ckpt is None:
        raise ValueError(
            f"key_path '{args.key_path}' is wrong or not found in checkpoint."
        )
else:
    ckpt = state
```

