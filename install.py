

# YAMLファイルのパス
yaml_file_path = 'jupyterlab_stable.yml'
# yamlファイルに書かれているパッケージ群の属性
name_list=["priorities", "packages", "pip"]
# 仮想環境のパス
virtual_env_path = '/opt/homebrew/anaconda3/envs/jupyterlab_stable'

import os
import subprocess
import yaml

def cmd(cmd):
    # Pythonでシェルコマンドを動かし、結果を取得する関数
    # 参考 : https://qiita.com/inatatsu_csg/items/40b11701d256a84a0510 
    import subprocess
    process = (subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]).decode('utf-8')[:-1].split("\n")
    return process

# YAMLファイルからパッケージのリストを読み込む
def load_packages_from_yaml(file_path, name_list=["dependencies"]):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        conda_packages=[]
        pip_packages=[]

        for name in name_list:
            for pack in data.get(name, []):
                if name == "pip":
                    pip_packages.append(pack)
                else:
                    conda_packages.append(pack)

        return conda_packages, pip_packages
# リストからcondaで読み込むパッケージを並べた文字列を作成
def make_package_list(packages):
    package_list=""
    for n in range(len(packages)):
        if not type(packages[n]) is dict:
            package_list += f"{packages[n]} "
            
    return(package_list)
            
# 仮想環境に、パッケージをインストールする
def install_packages(virtual_env_path, package_list, opt="", source="conda"):
    # 各パッケージをインストール
    if source == "conda":
        opt = f"-p {virtual_env_path} {package_list} {opt}"
    elif source == "pip":
        opt = f"{package_list}"
    print(f"{source} install {opt} >> logfile")
    cmd(f"{source} install {opt} >> logfile")

# YAMLファイルからパッケージのリストを読み込む
conda_packages, pip_packages = load_packages_from_yaml(yaml_file_path, name_list=name_list)
cmd(f"echo Executed on `date '+%Y-%m-%d %H:%M:%S'` > logfile")
if len(conda_packages) > 0:
    conda_packages = make_package_list (conda_packages)
    cmd(f"echo '\n'Packages to be installed by conda: >> logfile")
    cmd(f"echo {conda_packages} >>logfile")
    # パッケージをインストール
    install_packages(virtual_env_path, conda_packages, opt="-y", source="conda")

if len(pip_packages) > 0:    
    pip_packages = make_package_list (pip_packages)
    cmd(f"echo '\n'Packages to be installed by pip: >> logfile")
    cmd(f"echo {pip_packages} >>logfile")
    # パッケージをインストール
    install_packages(virtual_env_path, pip_packages, source="pip")

# 実行終了
print(f"Finished! - Check logs: {os.getcwd()}/logfile")