json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "bubble",
      "direction": "ltr",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "เกิดข้อผิดพลาด!",
            "weight": "bold",
            "size": "xxl",
            "color": "#FF2B85",
            "align": "center",
            "contents": []
          },
          {
            "type": "image",
            "url": "https://pandariders.info/wp-content/uploads/2023/10/Untitled-10.png",
            "margin": "none",
            "size": "3xl"
          }
        ]
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "ขออภัย ระบบไม่พบข้อมูล",
            "weight": "bold",
            "size": "xl",
            "color": "#FF2B85",
            "align": "center",
            "gravity": "center",
            "wrap": true,
            "contents": []
          },
          {
            "type": "text",
            "text": "กรุณาติดต่อเจ้าหน้าที่ผ่านทางแชทบนหน้าเว็บไซต์แลกรางวัล",
            "weight": "bold",
            "color": "#000000",
            "align": "center",
            "wrap": true,
            "contents": []
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "คลิกเพื่อติดต่อฯ",
              "uri": "https://ridershop.foodpanda.co.th/"
            },
            "color": "#FF2B85",
            "gravity": "center"
          }
        ]
      }
    }
  ]
}

"""