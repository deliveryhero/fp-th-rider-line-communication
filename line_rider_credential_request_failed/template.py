json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "เกิดข้อผิดพลาด! ขออภัย ระบบไม่พบข้อมูล",
      "contents": {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://pandariders.info/wp-content/uploads/2023/10/Untitled-10.png",
          "align": "center",
          "gravity": "center",
          "size": "xxl",
          "aspectRatio": "3:3",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "label": "Action",
            "uri": "https://linecorp.com/"
          }
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "md",
          "contents": [
            {
              "type": "text",
              "text": "เกิดข้อผิดพลาด!",
              "weight": "bold",
              "size": "xxl",
              "color": "#FF2B85",
              "align": "center",
              "gravity": "center",
              "wrap": true,
              "contents": []
            },
            {
              "type": "text",
              "text": "ขออภัย ระบบไม่พบข้อมูล",
              "weight": "bold",
              "color": "#FF2B85",
              "align": "center",
              "contents": []
            },
            {
              "type": "text",
              "text": "กรุณาติดต่อเจ้าหน้าที่ผ่านทางแชทบนหน้าเว็บไซต์แลกรางวัล",
              "align": "center",
              "wrap": true,
              "contents": []
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "horizontal",
          "flex": 1,
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "ติดต่อเจ้าหน้าที่",
                "uri": "https://ridershop.foodpanda.co.th/"
              },
              "color": "#FF2B85",
              "gravity": "center"
            }
          ]
        }
      }
    }
  ]
}

"""