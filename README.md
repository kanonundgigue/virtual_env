# pyenv 仮想環境の移植をする

## 事前準備

- mambaforgeをインストール

- 仮想環境を構築

```
mamba create -n py2023 python=3.11
```

- 仮想環境をactivate

```
mamba activate py2023
```


## 使い方

リポジトリをクローンする。

```
git@github.com:kanonundgigue/virtual_env.git ~/.virtual_env
cd ~/.virtual_env
```

パッケージインストール先となる仮想環境のpathを確認する。

```
mamba pyenv list
```

ぞろぞろと出てくる中で、

```
active env location : /home/kanon/.pyenv/versions/mambaforge-22.9.0-0/envs/py2023
```

といった行がみつかる。

仮想環境のパス(ここでは`/home/kanon/.pyenv/versions/mambaforge-22.9.0-0/envs/py2023`)を`my_virtual_env_path` に設定。

```
my_virtual_env_path="/home/kanon/.pyenv/versions/mambaforge-22.9.0-0/envs/py2023"
```

インストール用スクリプト`install.py`を作成。
```
sed -e "s|myenvpath|${my_virtual_env_path}|g" < install_sample.py > install.py
```

スクリプト内で使用されるパッケージを先にインストールしておく。

```
pip install pyyaml
```

スクリプト実行。

```
python install.py
```
