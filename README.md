# pyenv 仮想環境の移植をする

## このスクリプトを実行する前に

- 仮想環境を構築

```shell
	conda create -n jupyterlab_stable python=3.11
```

- 仮想環境をactivate

```shell
	pyenv activate jupyterlab_stable
```

- コマンド群をインストールするチャンネルを追加。

```shell
	conda config --add channels conda-forge
```

## 使い方

```shell
	python install.py
```