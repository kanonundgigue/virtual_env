# pyenv 仮想環境の移植をする

## 事前準備

- mambaforgeをインストール

- 仮想環境を構築

```
mamba create -n py2023 python=3.11
```

- 仮想環境をactivate

```
conda activate py2023
```


## 使い方

リポジトリをクローンする。

```
git clone git@github.com:kanonundgigue/virtual_env.git ~/.virtual_env
cd ~/.virtual_env
```

仮想環境のパス(ここでは`/home/kanon/.pyenv/versions/mambaforge-22.9.0-0/envs/py2023`)を`my_virtual_env_path` に設定。

```
my_virtual_env_path=`conda env list | grep py2023 | awk '{print $3}'`
echo $my_virtual_env_path
```

インストール用スクリプト`install.py`を作成。
```
sed -e "s|myenvpath|${my_virtual_env_path}|g" < install_sample.py > install.py
```

スクリプト内で使用されるパッケージを先にインストールしておく。

```
mamba install pyyaml
```

スクリプト実行。

```
python install.py
```
