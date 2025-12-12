# cicd-workshop-template
# CICD 体験ワークショップ用テンプレ（Python版・強化）

このリポジトリは「ローカルでは動くのにCIでは壊れている」状態を **確実に再現** し、
CICDの価値を体験するためのテンプレです。

## 何が“壊れている”の？

### 1) ローカルでは動くのに CI で壊れる（環境差異）
- ローカル：Python 3.11 を想定（`match/case` を使うため）
- CI：`.github/workflows/ci.yml` で Python 3.8 を指定（わざと）
  - その結果、CI上では **SyntaxError** になって落ちます（match/case は 3.10+）

### 2) テストが失敗する（アプリ側のバグ）
- `src/cicd_workshop/calculator.py` に軽いバグがあり、pytestが失敗します

### 3) CIが成功したときだけ動く CD（ダミー）
- `deploy.yml` は CI 成功時のみ実行されます（CDのゲート体験）

---

## ローカルでの実行（初心者向け）

### 1) Python 3.11 を用意（推奨）
### 2) 依存を入れる
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### 3) テスト実行（最初は失敗する）
```bash
pytest
```

---

## 参加者がやること（例）

1. GitHub Actions が落ちている理由をログで特定する（Pythonバージョン差）
2. `.github/workflows/ci.yml` の Python バージョンを直して CI を通す
3. その後、pytestの失敗（アプリ側バグ）を修正してテストを通す
4. CI成功時にCD（deploy.yml）が動くことを確認する
