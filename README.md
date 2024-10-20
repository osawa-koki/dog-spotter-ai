# dog-spotter-ai

🐩🐩🐩 犬を識別するAI！  

> [!WARNING]
> ローカルで動作させるためにはかなりのスペックが必要であるため、開発中止。

## 環境構築

DevContainerに入ります。  

### 1. Condaのセットアップ

```bash
conda init bash
conda update --name base --channel defaults conda --yes
conda create --name tf2 python=3.7 --yes
conda env list
conda activate tf2 # or `source activate tf2`
conda install tensorflow --yes
conda list --name tf2
python -c "import tensorflow as tf; print(tf.__version__)"
```

### 2. 必要なPythonパッケージのインストール

```bash
pip install -r ./requirements.txt
```

### 3. Gitのセットアップ (任意)

`/etc/apt/sources.list`を以下のように変更してください。  

```file
deb http://deb.debian.org/debian bullseye main
deb http://security.debian.org/debian-security bullseye-security main
deb http://deb.debian.org/debian bullseye-updates main
```

Gitをインストールします。  

```bash
apt-get update
apt-get install git
```

容量が足りない場合は、ホスト環境で以下のコマンドを実行してください。  

```bash
docker container prune
docker image prune
docker volume prune
docker system prune
```

## トラブルシューティング

### TensorFlowのインストール時に`Solving environment`で停止する

`conda install tensorflow`を実行したときに、`Solving environment`で停止する場合は、以下のコマンドを実行してください。  

```bash
conda clean --all
conda install tensorflow --yes --verbose
```
