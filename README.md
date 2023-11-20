# How to Use (added on Nov. 17, 2023)
プロジェクトを初めて起動する際には、以下の手順に従ってください。これにより、必要な環境を構築し、OpenAIのAPIを利用するためのキーを設定します。
## 1. 仮想環境のセットアップ
```bash
python -m venv openai-env
```
これにより、プロジェクト用の仮想環境が作成されます。仮想環境はプロジェクトごとに独立したPython実行環境を提供します。

## 2. 仮想環境のアクティベーション
```bash
source openai-env/bin/activate
```
仮想環境をアクティベートすることで、プロジェクト用のPython環境が有効になります。アクティベーション後、ターミナルプロンプトが仮想環境名で始まることを確認してください。

## 3. OpenAIライブラリのインストール
```bash
pip install --upgrade openai
```
必要なライブラリをインストールします。--upgradeオプションを使用することで、最新バージョンのOpenAIライブラリを取得します。

## 4. APIキーの生成と設定
### APIキーの生成
以下のリンクから生成可能\
https://platform.openai.com/api-keys
### APIキーの設定
```bash
export OPENAI_API_KEY='your-api-key-here'
```
OpenAIのAPIを使用するためには、APIキーが必要です。取得したAPIキーを上記のコマンドで環境変数に設定してください。これにより、プロジェクトがOpenAI APIにアクセスできるようになります。

以上で初回のセットアップが完了しました。以降、プロジェクトを起動する際には、仮想環境をアクティベートし、必要な環境変数を設定することで、OpenAI APIを利用できます。

## コードの実行
### Chat.completionの基本
```bash
Python basic.py
```

### Tool_callsの使い方
```bash
Python toolCalls.py
```