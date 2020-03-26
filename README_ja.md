[English](https://github.com/BonyChops/Game-Console-Activity-to-Discord)｜日本語 (Japanese)

# Game Console Activity to Discord

Discordであなたのゲーム機でのアクティビティを共有しよう！

# 機能

ローカルネットワーク上のゲーム機の起動を確認し、Discordのプロフィールから共有できます！

<div align="center">

<img src="https://raw.githubusercontent.com/bonychops/Game-Console-Activity-to-Discord/img/status.png" alt="Profile" title="Profile"><br><br>
<img src="https://raw.githubusercontent.com/bonychops/Game-Console-Activity-to-Discord/img/profile.png" alt="Profile" title="Profile">
</div>

# 対応デバイス

このソフトウェアは、自動的にインターネットに接続するゲーム機のほとんどに対応しています。       
例えば...

- Nintendo Switch
- Nintendo 3DS
- PS3
- PS4

# セットアップガイド（動画）

## Discordにゲーム機のステータスを出すアプリ作りました

[![](https://img.youtube.com/vi/5yHuvOHLPRc/0.jpg)](https://www.youtube.com/watch?v=5yHuvOHLPRc)

# セットアップ

## Windows

Windows用にビルドされたexeファイルから実行できます。

1. Releaseページからexeファイルをダウンロードする。
1. configの設定をする
1. `start.exe` を実行して、ソフトウェアを起動します。

## Linux/MacOS (and Windows)

Pythonを実行することでソフトウェアを動かすことができます。

1. Pythonをインストールする。
1. Gitをインストールする。
1. `git clone https://github.com/BonyChops/Game-Console-Activity-to-Discord.git` を実行し、ソースをクローンする。
1. `pip install` を実行し、依存関係をインストールする。
1. `python config.py` を実行し、ゲーム機の設定を行う
1. `python start.py` を実行し、ソフトウェアを起動します。

# configの設定

Windowsの場合は`config.exe`を、Linux/MacOSの場合は`config.py`を実行し、設定を開始します。

```
Configuration
[0] Add new console
[1] Delete console
[2] Exit

Type number [0-2]?
0
```

0. ゲーム機の追加
0. ゲーム機の削除
0. 終了

から、行いたい動作を選択する

```
Select your Game Console!
[0] Nintendo Switch
[1] Nintendo 3DS
[2] PS3
[3] PS4
[4] Others

Type number [0-4]?
0
```

追加するゲーム機を0-4で指定する。

```
Type IP address of your console!
192.168.1.30
Added!
------------------------------
[Nintendo Switch] IP 192.168.1.30
------------------------------
```

IPの設定を行う        
（詳しくは動画を確認してください）

```
Configuration
[0] Add new console
[1] Delete console
[2] Exit

Type number [0-2]?
2
Goodbye.
```

2で終了

# 自動起動の設定（Windowsのみ）

`startup.exe` を実行して、案内に従ってください。

# Package
### qwertyquerty/pypresence - Github

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)
