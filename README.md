# dog-spotter-ai

🐩🐩🐩 犬を識別するAI！  

## 環境構築

DevContainerに入ります。  

### 1. Condaのセットアップ

```bash
conda init bash
conda update --name base --channel defaults conda --yes
conda create -n tf2 python=3.7 --yes
conda activate tf2 # or `source activate tf2`
conda install tensorflow --yes
```

`python`コマンドで対話式インタプリタを起動させ、`import tensorflow`がエラーなく実行されることを確認します。  

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
apt-get install git --yes
```

容量が足りない場合は、ホスト環境で以下のコマンドを実行してください。  

```bash
docker container prune
docker image prune
docker volume prune
docker system prune
```
