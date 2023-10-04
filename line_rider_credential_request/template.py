json_object = """

{
  "to": "{line_user_id}",
  "messages": [
    {
      "type": "flex",
      "altText": "อีเมลและรหัสผ่านสำหรับเข้าสู่ระบบแลกคะแนนแบมบู",
      "contents": {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://pandariders.info/wp-content/uploads/2023/08/BAMBOO-REWARDS-MASCOT-160x160-1.png",
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
              "text": "อีเมลและรหัสผ่านสำหรับเข้าสู่ระบบแลกคะแนนแบมบู",
              "weight": "bold",
              "size": "xl",
              "gravity": "center",
              "wrap": true,
              "contents": []
            },
            {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "margin": "lg",
              "contents": [
                {
                  "type": "box",
                  "layout": "baseline",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "text",
                      "text": "อีเมล",
                      "size": "sm",
                      "color": "#AAAAAA",
                      "flex": 1,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "{rider_email}",
                      "size": "sm",
                      "color": "#666666",
                      "flex": 4,
                      "wrap": true,
                      "contents": []
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "text",
                      "text": "รหัสผ่าน",
                      "size": "sm",
                      "color": "#AAAAAA",
                      "flex": 1,
                      "contents": []
                    },
                    {
                      "type": "text",
                      "text": "{rider_password}",
                      "size": "sm",
                      "color": "#666666",
                      "flex": 4,
                      "wrap": true,
                      "contents": []
                    }
                  ]
                }
              ]
            },
            {
              "type": "text",
              "text": "เพื่อความปลอดภัยของข้อมูล กรุณาเก็บไว้เป็นความลับ!",
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
                "label": "ไปยังระบบแลกรางวัลฯ",
                "uri": "https://ridershop.foodpanda.co.th/"
              },
              "color": "#FF2B855B",
              "gravity": "center"
            }
          ]
        }
      }
    }
  ]
}

"""