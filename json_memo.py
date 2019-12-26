""" 認可コード

e79a2417889d48a3bd5d6ea0b4a6a1633428abec9d5c46548afadd383ae67932

"""

""" アクセストークン取得

https://accounts.secure.freee.co.jp/public_api/authorize?client_id=054b9c53d65500f4cf58afd558d2c6b83a44a13a603f73cae059f6091a1ae10e&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&response_type=token

"""
# errorを黙らせる
null = 0

# freee
{
  "client_id" : "054b9c53d65500f4cf58afd558d2c6b83a44a13a603f73cae059f6091a1ae10e",
  "secret_key" : "42d22e8dd9b9f4fe551d3221c9789dff944c7c84dd8f5cbba62dc69e81d23324"
}

{
  "companies": [
    {
      "id": 2031596,
      "name": null,
      "name_kana": null,
      "display_name": "事業所名（未設定）",
      "role": "admin"
    },
    {
      "id": 2031597,
      "name": null,
      "name_kana": null,
      "display_name": "事業所名（未設定）",
      "role": "admin"
    },
    {
      "id": 2031639,
      "name": null,
      "name_kana": null,
      "display_name": "法人ベーシックプラン: 開発用テスト環境",
      "role": "admin"
    }
  ]
}

# 請求書json例
"""削除したパラメータ
  id,
  partner_code, parner_name, reduced_vat, partner_prefecture_code,
  partner_address1, partner_address2, pertner_long_name,
  company_zipcode, company_address1, company_address2, 
  total_amount, total_vat, sub_total, payment_date,
  partner_prefecture_name, section_name,
  company_prefecture_code, company_prefecture_code, company_contact_info,
  deal_id,
"""
{
      "company_id": 2031639,
      "issue_date": "2019-11-01",
      "partner_id": 21686589,
      "invoice_number": "80",
      "title": "請求書",
      "due_date": "2019-11-22",
      "booking_date": "2019-11-11",
      "description": "あああああ",
      "invoice_status": "issue",
      "payment_status": "unsettled",
      "partner_title": "(空白)",
      "partner_contact_info": "い",
      "company_name": "法人ベーシックプラン: 開発用テスト環境",
      "payment_type": "direct_debit",
      "payment_bank_info": "Imaginary Bank 駒場支店",
      "message": "下記の通りご請求申し上げます。",
      "notes": "毎度ありがとうございます",
      "invoice_layout": "default_classic",
      "tax_entry_method": "exclusive",
      "invoice_contents": [
        {
          "id": 43977213,
          "order": 433,
          "type": "normal",
          "qty": 20,
          "unit": "個",
          "unit_price": 50000,
          "amount": 55000,
          "vat": 100000,
          "description": "ぼったくり",
          "account_item_id": 325107158,
          "account_item_name": "売上高",
          "tax_code": 129,
          "item_id": 168881729,
          "item_name": "ポスターデザイン",
          "tag_ids": [],
          "tag_names": []
        },
        {
          "id": 43977213,
          "order": 433,
          "type": "normal",
          "qty": 20,
          "unit": "個",
          "unit_price": 10000,
          "amount": 11000,
          "vat": 20000,
          "description": "ぼったくり2",
          "account_item_id": 325107158,
          "account_item_name": "売上高",
          "tax_code": 129,
          "item_id": 168881729,
          "item_name": "ポスターデザイン",
          "tag_ids": [],
          "tag_names": []
        }
      ]
    }
