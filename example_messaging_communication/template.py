json_object = """
{
    "to": "{LineUserID}",
    "messages": [
        {
            "type": "flex",
            "altText": "รายงานผลประกอบการรายสัปดาห์",
            "contents":
{
  "type": "bubble",
  "size": "giga",
  "direction": "ltr",
  "header": {
    "type": "box",
    "layout": "horizontal",
    "height": "75px",
    "contents": [
      {
        "type": "image",
        "url": "https://drive.google.com/uc?export=view&id=1rdAZNj4G-IQtBBlRL_Coh3Si7IyafmiQ",
        "margin": "none",
        "align": "center",
        "size": "full",
        "aspectRatio": "50:10",
        "aspectMode": "cover",
        "position": "absolute",
        "offsetTop": "0px",
        "offsetBottom": "0px",
        "offsetStart": "0px",
        "offsetEnd": "0px"
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "position": "relative",
    "height": "955px",
    "contents": [
      {
        "type": "text",
        "text": "เรียน ร้าน {vendor_name}",
        "weight": "bold",
        "size": "md",
        "align": "start",
        "gravity": "top",
        "wrap": true,
        "contents": [
          {
            "type": "span",
            "text": "เรียน ร้าน ",
            "size": "md",
            "weight": "bold"
          },
          {
            "type": "span",
            "text": "{vendor_name}",
            "size": "md",
            "weight": "regular"
          }
        ]
      },
      {
        "type": "text",
        "text": "รหัส {vendor_code}",
        "weight": "bold",
        "size": "md",
        "align": "start",
        "gravity": "top",
        "contents": [
          {
            "type": "span",
            "text": "รหัส ",
            "size": "md",
            "weight": "bold"
          },
          {
            "type": "span",
            "text": "{vendor_code}",
            "size": "md",
            "weight": "regular"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "xl",
        "color": "#CACACAFF"
      },
      {
        "type": "text",
        "text": "คะแนนร้านค้ายอดเยี่ยมคือ {ihs_score} / 5 คะแนน",
        "wrap": true,
        "offsetTop": "10px",
        "contents": [
          {
            "type": "span",
            "text": "คะแนนร้านค้ายอดเยี่ยม",
            "color": "#FF2B85"
          },
          {
            "type": "span",
            "text": "คือ {ihs_score} / 5 คะแนน"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "spacing": "xxl",
        "offsetTop": "17px",
        "borderWidth": "1px",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "width": "145px",
            "height": "100px",
            "backgroundColor": "#FECCDCFF",
            "borderColor": "#FECCDCFF",
            "cornerRadius": "md",
            "contents": [
              {
                "type": "text",
                "text": "จำนวนลูกค้า",
                "weight": "bold",
                "size": "sm",
                "align": "center",
                "offsetTop": "10px",
                "contents": []
              },
              {
                "type": "text",
                "text": "{customers} คน",
                "weight": "bold",
                "size": "xs",
                "color": "#FF2B85",
                "align": "center",
                "gravity": "center",
                "wrap": false,
                "offsetTop": "15px",
                "contents": []
              },
              {
                "type": "text",
                "text": "{perc_customer_growth}%",
                "weight": "regular",
                "size": "xxs",
                "align": "center",
                "wrap": true,
                "offsetTop": "20px",
                "contents": []
              },
              {
                "type": "text",
                "text": "เทียบกับสัปดาห์ก่อน",
                "weight": "regular",
                "size": "xxs",
                "align": "center",
                "wrap": true,
                "offsetTop": "20px",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "spacing": "xs",
            "margin": "xs",
            "position": "relative",
            "width": "5px",
            "contents": [
              {
                "type": "separator",
                "color": "#FFFFFFFF"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "width": "145px",
            "height": "100px",
            "backgroundColor": "#FECCDCFF",
            "borderColor": "#FECCDCFF",
            "cornerRadius": "md",
            "contents": [
              {
                "type": "text",
                "text": "ออเดอร์ที่สำเร็จ",
                "weight": "bold",
                "size": "sm",
                "align": "center",
                "offsetTop": "10px",
                "contents": []
              },
              {
                "type": "text",
                "text": "{valid_orders} ออเดอร์",
                "weight": "bold",
                "size": "xs",
                "color": "#FF2B85",
                "align": "center",
                "gravity": "center",
                "offsetTop": "15px",
                "contents": []
              },
              {
                "type": "text",
                "text": "{perc_order_growth}%",
                "weight": "regular",
                "size": "xxs",
                "align": "center",
                "gravity": "center",
                "wrap": true,
                "offsetTop": "20px",
                "contents": []
              },
              {
                "type": "text",
                "text": "เทียบกับสัปดาห์ก่อน",
                "weight": "regular",
                "size": "xxs",
                "align": "center",
                "wrap": true,
                "offsetTop": "20px",
                "contents": []
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "position": "relative",
        "offsetTop": "22px",
        "height": "60px",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "เพิ่มยอดขายด้วย การดึงดูดลูกค้าใหม่ คลิก",
                "size": "xxs",
                "wrap": true,
                "action": {
                  "type": "uri",
                  "label": "คลิก",
                  "uri": "https://bit.ly/linebwpdb"
                },
                "position": "relative",
                "contents": [
                  {
                    "type": "span",
                    "text": "เพิ่มยอดขายด้วย "
                  },
                  {
                    "type": "span",
                    "text": "การดึงดูดลูกค้าใหม่ คลิก",
                    "color": "#FF2B85FF",
                    "weight": "bold"
                  }
                ]
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "spacing": "xs",
            "margin": "xs",
            "position": "relative",
            "width": "20px",
            "contents": [
              {
                "type": "separator",
                "color": "#FFFFFFFF"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "มอบ ส่วนลด เพื่อเพิ่มออเดอร์ซื้อได้ถึง 2 เท่า คลิก",
                "size": "xxs",
                "wrap": true,
                "action": {
                  "type": "uri",
                  "label": "คลิก",
                  "uri": "https://bit.ly/linebwdisc"
                },
                "contents": [
                  {
                    "type": "span",
                    "text": "มอบ"
                  },
                  {
                    "type": "span",
                    "text": " ส่วนลด ",
                    "color": "#FF2B85FF",
                    "weight": "bold"
                  },
                  {
                    "type": "span",
                    "text": "เพื่อเพิ่มออเดอร์ได้ถึง 2 เท่า "
                  },
                  {
                    "type": "span",
                    "text": "คลิก ",
                    "color": "#FF2B85FF",
                    "weight": "bold"
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "offsetTop": "10px",
        "height": "80px",
        "backgroundColor": "#EBEBEB",
        "cornerRadius": "md",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "offsetTop": "0px",
            "width": "120px",
            "contents": [
              {
                "type": "text",
                "text": "3 เมนู",
                "color": "#FF2B85",
                "align": "center",
                "gravity": "center",
                "offsetTop": "15px",
                "contents": [
                  {
                    "type": "span",
                    "text": "3 เมนู",
                    "color": "#FF2B85"
                  }
                ]
              },
              {
                "type": "text",
                "text": "ที่ขายดีที่สุด",
                "color": "#FF2B85",
                "align": "center",
                "gravity": "center",
                "offsetTop": "15px",
                "contents": [
                  {
                    "type": "span",
                    "text": "ที่ขายดีที่สุด",
                    "color": "#FF2B85"
                  }
                ]
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "offsetTop": "10px",
            "offsetStart": "0px",
            "height": "90px",
            "contents": [
              {
                "type": "text",
                "text": "1. {top1_best_seller}",
                "wrap": true,
                "contents": [
                  {
                    "type": "span",
                    "text": "1. {top1_best_seller}",
                    "size": "xs"
                  }
                ]
              },
              {
                "type": "text",
                "text": "2. {top2_best_seller}",
                "wrap": true,
                "contents": [
                  {
                    "type": "span",
                    "text": "2. {top2_best_seller}",
                    "size": "xs"
                  }
                ]
              },
              {
                "type": "text",
                "text": "3. {top3_best_seller}",
                "wrap": true,
                "contents": [
                  {
                    "type": "span",
                    "text": "3. {top3_best_seller}",
                    "size": "xs"
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "offsetTop": "40px",
        "height": "80px",
        "borderWidth": "1px",
        "borderColor": "#FF2B85FF",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "width": "83px",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "จำนวนออเดอร์ที่ถูกปฏิเสธ",
                "weight": "bold",
                "size": "xs",
                "color": "#FF2B85",
                "align": "start",
                "gravity": "center",
                "wrap": true,
                "offsetStart": "3px",
                "offsetEnd": "3px",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "width": "80px",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "{failed_orders}",
                "size": "xs",
                "align": "center",
                "gravity": "center",
                "offsetTop": "10px",
                "contents": []
              },
              {
                "type": "text",
                "text": "ออเดอร์",
                "size": "xs",
                "align": "center",
                "gravity": "center",
                "offsetTop": "15px",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "ลดการปฏิเสธออเดอร์ โดยใช้งานเครื่องมือ รายงานผลประกอบการ",
                "size": "xs",
                "gravity": "center",
                "wrap": true,
                "action": {
                  "type": "uri",
                  "label": "รายงานผลประกอบการ",
                  "uri": "https://bit.ly/linebwreports"
                },
                "offsetStart": "2px",
                "offsetEnd": "2px",
                "contents": [
                  {
                    "type": "span",
                    "text": "{improve_order} "
                  },
                  {
                    "type": "span",
                    "text": "คลิก",
                    "weight": "regular"
                  },
                  {
                    "type": "span",
                    "text": "ที่นี่",
                    "color": "#FF2B85FF",
                    "weight": "bold"
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "offsetTop": "38px",
        "height": "80px",
        "borderWidth": "1px",
        "borderColor": "#FF2B85FF",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "width": "83px",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "เมนูที่ถูกปฏิเสธบ่อยที่สุด",
                "weight": "bold",
                "size": "xs",
                "color": "#FF2B85FF",
                "align": "start",
                "gravity": "center",
                "wrap": true,
                "offsetStart": "3px",
                "offsetEnd": "3px",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "width": "80px",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "{top_failed_product}",
                "size": "xs",
                "align": "center",
                "gravity": "center",
                "wrap": true,
                "offsetTop": "5px",
                "offsetStart": "2px",
                "offsetEnd": "2px",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "{improve_menu} คลิกที่นี่",
                "size": "xs",
                "align": "start",
                "gravity": "center",
                "wrap": true,
                "action": {
                  "type": "uri",
                  "label": "ที่นี่",
                  "uri": "https://bit.ly/linebwmenu"
                },
                "offsetStart": "2px",
                "offsetEnd": "2px",
                "contents": [
                  {
                    "type": "span",
                    "text": "{improve_menu} "
                  },
                  {
                    "type": "span",
                    "text": "คลิก",
                    "weight": "regular"
                  },
                  {
                    "type": "span",
                    "text": "ที่นี่",
                    "color": "#FF2B85FF",
                    "weight": "bold"
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "offsetTop": "36px",
        "height": "110px",
        "borderWidth": "1px",
        "borderColor": "#FF2B85FF",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "width": "83px",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "เหตุผลหลักที่ปฏิเสธออเดอร์",
                "weight": "bold",
                "size": "xs",
                "color": "#FF2B85FF",
                "align": "start",
                "gravity": "center",
                "wrap": true,
                "offsetStart": "3px",
                "offsetEnd": "3px",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "width": "80px",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "{top_failed_reason}",
                "size": "xs",
                "align": "center",
                "gravity": "center",
                "wrap": true,
                "offsetStart": "2px",
                "offsetEnd": "2px",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "{improve_top_failed_reason} คลิกที่นี่",
                "size": "xs",
                "align": "start",
                "gravity": "center",
                "wrap": true,
                "action": {
                  "type": "uri",
                  "label": "ที่นี่",
                  "uri": "https://bit.ly/linebwfailuni"
                },
                "offsetStart": "2px",
                "offsetEnd": "2px",
                "contents": [
                  {
                    "type": "span",
                    "text": "{improve_top_failed_reason} "
                  },
                  {
                    "type": "span",
                    "text": "คลิก"
                  },
                  {
                    "type": "span",
                    "text": "ที่นี่",
                    "color": "#FF2B85FF",
                    "weight": "bold"
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "offsetTop": "34px",
        "height": "110px",
        "borderWidth": "1px",
        "borderColor": "#FF2B85FF",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "width": "83px",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "อัตราการปิดร้านในเวลาทำการ 7 วันที่ผ่านมา",
                "weight": "bold",
                "size": "xs",
                "color": "#FF2B85FF",
                "align": "start",
                "gravity": "center",
                "wrap": true,
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "width": "80px",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "{perc_offline}",
                "size": "xs",
                "align": "center",
                "gravity": "center",
                "wrap": true,
                "offsetTop": "28px",
                "offsetStart": "2px",
                "offsetEnd": "2px",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "เปิดร้านมากขึ้น เพื่อให้ได้ออเดอร์ที่มากขึ้น  ศึกษา เคล็ดลับที่เป็นประโยชน์",
                "size": "xs",
                "align": "start",
                "gravity": "center",
                "wrap": true,
                "action": {
                  "type": "uri",
                  "label": "เคล็ดลับที่เป็นประโย",
                  "uri": "https://bit.ly/linebwpfmuni"
                },
                "contents": [
                  {
                    "type": "span",
                    "text": "เปิดร้านมากขึ้น เพื่อให้ได้ออเดอร์ที่มากขึ้น  ศึกษา"
                  },
                  {
                    "type": "span",
                    "text": "เคล็ดลับที่เป็นประโยชน์",
                    "color": "#FF2B85FF",
                    "weight": "bold"
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "offsetTop": "32px",
        "height": "110px",
        "borderWidth": "1px",
        "borderColor": "#FF2B85FF",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "width": "83px",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "สาเหตุที่ปิดร้านในเวลาทำการ",
                "weight": "bold",
                "size": "xs",
                "color": "#FF2B85FF",
                "align": "start",
                "gravity": "center",
                "wrap": true,
                "offsetStart": "3px",
                "offsetEnd": "3px",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "width": "80px",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "{top_offline_reason}",
                "size": "xs",
                "align": "center",
                "gravity": "center",
                "wrap": true,
                "offsetTop": "0px",
                "offsetStart": "2px",
                "offsetEnd": "2px",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "borderWidth": "1px",
            "borderColor": "#FF2B85FF",
            "contents": [
              {
                "type": "text",
                "text": "{improve_top_offline_reason} คลิกที่นี่",
                "size": "xs",
                "align": "start",
                "gravity": "center",
                "wrap": true,
                "action": {
                  "type": "uri",
                  "label": "ที่นี่",
                  "uri": "https://bit.ly/lineoffuni"
                },
                "offsetStart": "2px",
                "offsetEnd": "2px",
                "contents": [
                  {
                    "type": "span",
                    "text": "{improve_top_offline_reason} "
                  },
                  {
                    "type": "span",
                    "text": "คลิก"
                  },
                  {
                    "type": "span",
                    "text": "ที่นี่",
                    "color": "#FF2B85FF",
                    "weight": "bold"
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "offsetTop": "35px",
        "contents": [
          {
            "type": "text",
            "text": "*รายงานผลประกอบการช่วงวันที่ {first_date} ถึง {last_date} ",
            "size": "xxs",
            "align": "start",
            "style": "italic",
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "offsetTop": "35px",
        "contents": [
          {
            "type": "text",
            "text": "**คุณจะได้รับรายงานนี้ภายใน 60 วันแรกหลังเข้าร่วมกับ foodpanda เท่านั้น",
            "size": "xxs",
            "align": "start",
            "wrap": true,
            "contents": []
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "offsetTop": "40px",
        "contents": [
          {
            "type": "text",
            "text": "หากคุณต้องการแจ้งปัญหาเกี่ยวกับรายงานฉบับนี้ คลิกที่นี่",
            "size": "xs",
            "wrap": true,
            "action": {
              "type": "uri",
              "label": "คลิกที่นี่",
              "uri": "https://docs.google.com/forms/d/e/1FAIpQLScC8VpIJ2lDJQH6fYNN_s_cxfCtv43TCBLLAGbwaQa28-yYoQ/viewform"
            },
            "contents": [
              {
                "type": "span",
                "text": "หากคุณต้องการ"
              },
              {
                "type": "span",
                "text": "แจ้งปัญหา",
                "color": "#FF2B85FF",
                "weight": "bold"
              },
              {
                "type": "span",
                "text": "เกี่ยวกับรายงานฉบับนี้ คลิก"
              },
              {
                "type": "span",
                "text": "ที่นี่",
                "color": "#FF2B85FF",
                "weight": "bold"
              }
            ]
          }
        ]
      }
    ]
  }
}
    }
  ],
    "customAggregationUnits": [
        "IncubationWeeklyReport"
    ]
}

"""



# json_object = """
# {
#     "to": "{LineUserID}",
#     "messages": [
#         {
#             "type": "flex",
#             "altText": "รายงานผลประกอบการรายสัปดาห์",
#             "contents":
# {
#   "type": "bubble",
#   "size": "giga",
#   "direction": "ltr",
#   "header": {
#     "type": "box",
#     "layout": "horizontal",
#     "height": "75px",
#     "contents": [
#       {
#         "type": "image",
#         "url": "https://drive.google.com/uc?export=view&id=1rdAZNj4G-IQtBBlRL_Coh3Si7IyafmiQ",
#         "margin": "none",
#         "align": "center",
#         "size": "full",
#         "aspectRatio": "50:10",
#         "aspectMode": "cover",
#         "position": "absolute",
#         "offsetTop": "0px",
#         "offsetBottom": "0px",
#         "offsetStart": "0px",
#         "offsetEnd": "0px"
#       }
#     ]
#   },
#   "body": {
#     "type": "box",
#     "layout": "vertical",
#     "position": "relative",
#     "height": "940px",
#     "contents": [
#       {
#         "type": "text",
#         "text": "เรียน ร้าน {vendor_name}",
#         "weight": "bold",
#         "size": "md",
#         "align": "start",
#         "gravity": "top",
#         "wrap": true,
#         "contents": [
#           {
#             "type": "span",
#             "text": "เรียน ร้าน ",
#             "size": "md",
#             "weight": "bold"
#           },
#           {
#             "type": "span",
#             "text": "{vendor_name}",
#             "size": "md",
#             "weight": "regular"
#           }
#         ]
#       },
#       {
#         "type": "text",
#         "text": "รหัส {vendor_code}",
#         "weight": "bold",
#         "size": "md",
#         "align": "start",
#         "gravity": "top",
#         "contents": [
#           {
#             "type": "span",
#             "text": "รหัส ",
#             "size": "md",
#             "weight": "bold"
#           },
#           {
#             "type": "span",
#             "text": "{vendor_code}",
#             "size": "md",
#             "weight": "regular"
#           }
#         ]
#       },
#       {
#         "type": "separator",
#         "margin": "xl",
#         "color": "#CACACAFF"
#       },
#       {
#         "type": "text",
#         "text": "คะแนนร้านค้ายอดเยี่ยมคือ {ihs_score} / 5 คะแนน",
#         "wrap": true,
#         "offsetTop": "10px",
#         "contents": [
#           {
#             "type": "span",
#             "text": "คะแนนร้านค้ายอดเยี่ยม",
#             "color": "#FF2B85"
#           },
#           {
#             "type": "span",
#             "text": "คือ {ihs_score} / 5 คะแนน"
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "spacing": "xxl",
#         "offsetTop": "17px",
#         "borderWidth": "1px",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "vertical",
#             "width": "145px",
#             "height": "100px",
#             "backgroundColor": "#FECCDCFF",
#             "borderColor": "#FECCDCFF",
#             "cornerRadius": "md",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "จำนวนลูกค้า",
#                 "weight": "bold",
#                 "size": "sm",
#                 "align": "center",
#                 "offsetTop": "10px",
#                 "contents": []
#               },
#               {
#                 "type": "text",
#                 "text": "{customers} คน",
#                 "weight": "bold",
#                 "size": "xs",
#                 "color": "#FF2B85",
#                 "align": "center",
#                 "gravity": "center",
#                 "wrap": false,
#                 "offsetTop": "15px",
#                 "contents": []
#               },
#               {
#                 "type": "text",
#                 "text": "{perc_customer_growth}%",
#                 "weight": "regular",
#                 "size": "xxs",
#                 "align": "center",
#                 "wrap": true,
#                 "offsetTop": "20px",
#                 "contents": []
#               },
#               {
#                 "type": "text",
#                 "text": "เทียบกับสัปดาห์ก่อน",
#                 "weight": "regular",
#                 "size": "xxs",
#                 "align": "center",
#                 "wrap": true,
#                 "offsetTop": "20px",
#                 "contents": []
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "spacing": "xs",
#             "margin": "xs",
#             "position": "relative",
#             "width": "5px",
#             "contents": [
#               {
#                 "type": "separator",
#                 "color": "#FFFFFFFF"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "width": "145px",
#             "height": "100px",
#             "backgroundColor": "#FECCDCFF",
#             "borderColor": "#FECCDCFF",
#             "cornerRadius": "md",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "ออเดอร์ที่สำเร็จ",
#                 "weight": "bold",
#                 "size": "sm",
#                 "align": "center",
#                 "offsetTop": "10px",
#                 "contents": []
#               },
#               {
#                 "type": "text",
#                 "text": "{valid_orders} ออเดอร์",
#                 "weight": "bold",
#                 "size": "xs",
#                 "color": "#FF2B85",
#                 "align": "center",
#                 "gravity": "center",
#                 "offsetTop": "15px",
#                 "contents": []
#               },
#               {
#                 "type": "text",
#                 "text": "{perc_order_growth}%",
#                 "weight": "regular",
#                 "size": "xxs",
#                 "align": "center",
#                 "gravity": "center",
#                 "wrap": true,
#                 "offsetTop": "20px",
#                 "contents": []
#               },
#               {
#                 "type": "text",
#                 "text": "เทียบกับสัปดาห์ก่อน",
#                 "weight": "regular",
#                 "size": "xxs",
#                 "align": "center",
#                 "wrap": true,
#                 "offsetTop": "20px",
#                 "contents": []
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "position": "relative",
#         "offsetTop": "22px",
#         "height": "60px",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "เพิ่มยอดขายด้วย การดึงดูดลูกค้าใหม่ คลิก",
#                 "size": "xxs",
#                 "wrap": true,
#                 "action": {
#                   "type": "uri",
#                   "label": "คลิก",
#                   "uri": "https://bit.ly/linebwpdb"
#                 },
#                 "position": "relative",
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "เพิ่มยอดขายด้วย "
#                   },
#                   {
#                     "type": "span",
#                     "text": "การดึงดูดลูกค้าใหม่ คลิก",
#                     "color": "#FF2B85FF",
#                     "weight": "bold"
#                   }
#                 ]
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "spacing": "xs",
#             "margin": "xs",
#             "position": "relative",
#             "width": "20px",
#             "contents": [
#               {
#                 "type": "separator",
#                 "color": "#FFFFFFFF"
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "มอบ ส่วนลด เพื่อเพิ่มออเดอร์ซื้อได้ถึง 2 เท่า คลิก",
#                 "size": "xxs",
#                 "wrap": true,
#                 "action": {
#                   "type": "uri",
#                   "label": "คลิก",
#                   "uri": "https://bit.ly/linebwdisc"
#                 },
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "มอบ"
#                   },
#                   {
#                     "type": "span",
#                     "text": " ส่วนลด ",
#                     "color": "#FF2B85FF",
#                     "weight": "bold"
#                   },
#                   {
#                     "type": "span",
#                     "text": "เพื่อเพิ่มออเดอร์ได้ถึง 2 เท่า "
#                   },
#                   {
#                     "type": "span",
#                     "text": "คลิก ",
#                     "color": "#FF2B85FF",
#                     "weight": "bold"
#                   }
#                 ]
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "offsetTop": "10px",
#         "height": "80px",
#         "backgroundColor": "#EBEBEB",
#         "cornerRadius": "md",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "vertical",
#             "offsetTop": "0px",
#             "width": "120px",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "3 เมนู",
#                 "color": "#FF2B85",
#                 "align": "center",
#                 "gravity": "center",
#                 "offsetTop": "15px",
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "3 เมนู",
#                     "color": "#FF2B85"
#                   }
#                 ]
#               },
#               {
#                 "type": "text",
#                 "text": "ที่ขายดีที่สุด",
#                 "color": "#FF2B85",
#                 "align": "center",
#                 "gravity": "center",
#                 "offsetTop": "15px",
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "ที่ขายดีที่สุด",
#                     "color": "#FF2B85"
#                   }
#                 ]
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "offsetTop": "10px",
#             "offsetStart": "0px",
#             "height": "90px",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "1. {top1_best_seller}",
#                 "wrap": true,
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "1. {top1_best_seller}",
#                     "size": "xs"
#                   }
#                 ]
#               },
#               {
#                 "type": "text",
#                 "text": "2. {top2_best_seller}",
#                 "wrap": true,
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "2. {top2_best_seller}",
#                     "size": "xs"
#                   }
#                 ]
#               },
#               {
#                 "type": "text",
#                 "text": "3. {top3_best_seller}",
#                 "wrap": true,
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "3. {top3_best_seller}",
#                     "size": "xs"
#                   }
#                 ]
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "offsetTop": "40px",
#         "height": "80px",
#         "borderWidth": "1px",
#         "borderColor": "#FF2B85FF",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "width": "83px",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "จำนวนออเดอร์ที่ถูกปฏิเสธ",
#                 "weight": "bold",
#                 "size": "xs",
#                 "color": "#FF2B85",
#                 "align": "start",
#                 "gravity": "center",
#                 "wrap": true,
#                 "offsetStart": "3px",
#                 "offsetEnd": "3px",
#                 "contents": []
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "width": "80px",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "{failed_orders}",
#                 "size": "xs",
#                 "align": "center",
#                 "gravity": "center",
#                 "offsetTop": "10px",
#                 "contents": []
#               },
#               {
#                 "type": "text",
#                 "text": "ออเดอร์",
#                 "size": "xs",
#                 "align": "center",
#                 "gravity": "center",
#                 "offsetTop": "15px",
#                 "contents": []
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "ลดการปฏิเสธออเดอร์ โดยใช้งานเครื่องมือ รายงานผลประกอบการ",
#                 "size": "xs",
#                 "gravity": "center",
#                 "wrap": true,
#                 "action": {
#                   "type": "uri",
#                   "label": "รายงานผลประกอบการ",
#                   "uri": "https://bit.ly/linebwreports"
#                 },
#                 "offsetStart": "2px",
#                 "offsetEnd": "2px",
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "{improve_order}"
#                   },
#                   {
#                     "type": "span",
#                     "text": "คลิก",
#                     "weight": "regular"
#                   },
#                   {
#                     "type": "span",
#                     "text": "ที่นี่",
#                     "color": "#FF2B85FF",
#                     "weight": "bold"
#                   }
#                 ]
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "offsetTop": "38px",
#         "height": "80px",
#         "borderWidth": "1px",
#         "borderColor": "#FF2B85FF",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "width": "83px",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "เมนูที่ถูกปฏิเสธบ่อยที่สุด",
#                 "weight": "bold",
#                 "size": "xs",
#                 "color": "#FF2B85FF",
#                 "align": "start",
#                 "gravity": "center",
#                 "wrap": true,
#                 "offsetStart": "3px",
#                 "offsetEnd": "3px",
#                 "contents": []
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "width": "80px",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "{top_failed_product}",
#                 "size": "xs",
#                 "align": "center",
#                 "gravity": "center",
#                 "wrap": true,
#                 "offsetTop": "5px",
#                 "offsetStart": "2px",
#                 "offsetEnd": "2px",
#                 "contents": []
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "{improve_menu} คลิกที่นี่",
#                 "size": "xs",
#                 "align": "start",
#                 "gravity": "center",
#                 "wrap": true,
#                 "action": {
#                   "type": "uri",
#                   "label": "ที่นี่",
#                   "uri": "https://bit.ly/linebwmenu"
#                 },
#                 "offsetStart": "2px",
#                 "offsetEnd": "2px",
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "{improve_menu}"
#                   },
#                   {
#                     "type": "span",
#                     "text": "คลิก",
#                     "weight": "regular"
#                   },
#                   {
#                     "type": "span",
#                     "text": "ที่นี่",
#                     "color": "#FF2B85FF",
#                     "weight": "bold"
#                   }
#                 ]
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "offsetTop": "36px",
#         "height": "110px",
#         "borderWidth": "1px",
#         "borderColor": "#FF2B85FF",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "width": "83px",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "เหตุผลหลักที่ปฏิเสธออเดอร์",
#                 "weight": "bold",
#                 "size": "xs",
#                 "color": "#FF2B85FF",
#                 "align": "start",
#                 "gravity": "center",
#                 "wrap": true,
#                 "offsetStart": "3px",
#                 "offsetEnd": "3px",
#                 "contents": []
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "width": "80px",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "{top_failed_reason}",
#                 "size": "xs",
#                 "align": "center",
#                 "gravity": "center",
#                 "wrap": true,
#                 "offsetStart": "2px",
#                 "offsetEnd": "2px",
#                 "contents": []
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "{improve_top_failed_reason} คลิกที่นี่",
#                 "size": "xs",
#                 "align": "start",
#                 "gravity": "center",
#                 "wrap": true,
#                 "action": {
#                   "type": "uri",
#                   "label": "ที่นี่",
#                   "uri": "https://bit.ly/linebwfailuni"
#                 },
#                 "offsetStart": "2px",
#                 "offsetEnd": "2px",
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "{improve_top_failed_reason}"
#                   },
#                   {
#                     "type": "span",
#                     "text": "คลิก"
#                   },
#                   {
#                     "type": "span",
#                     "text": "ที่นี่",
#                     "color": "#FF2B85FF",
#                     "weight": "bold"
#                   }
#                 ]
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "offsetTop": "34px",
#         "height": "110px",
#         "borderWidth": "1px",
#         "borderColor": "#FF2B85FF",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "width": "83px",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "อัตราการปิดร้านในเวลาทำการ 7 วันที่ผ่านมา",
#                 "weight": "bold",
#                 "size": "xs",
#                 "color": "#FF2B85FF",
#                 "align": "start",
#                 "gravity": "center",
#                 "wrap": true,
#                 "contents": []
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "vertical",
#             "width": "80px",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "{perc_offline}",
#                 "size": "xs",
#                 "align": "center",
#                 "gravity": "center",
#                 "wrap": true,
#                 "offsetTop": "28px",
#                 "offsetStart": "2px",
#                 "offsetEnd": "2px",
#                 "contents": []
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "เปิดร้านมากขึ้น เพื่อให้ได้ออเดอร์ที่มากขึ้น  ศึกษา เคล็ดลับที่เป็นประโยชน์",
#                 "size": "xs",
#                 "align": "start",
#                 "gravity": "center",
#                 "wrap": true,
#                 "action": {
#                   "type": "uri",
#                   "label": "เคล็ดลับที่เป็นประโย",
#                   "uri": "https://bit.ly/linebwpfmuni"
#                 },
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "เปิดร้านมากขึ้น เพื่อให้ได้ออเดอร์ที่มากขึ้น  ศึกษา"
#                   },
#                   {
#                     "type": "span",
#                     "text": "เคล็ดลับที่เป็นประโยชน์",
#                     "color": "#FF2B85FF",
#                     "weight": "bold"
#                   }
#                 ]
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "horizontal",
#         "offsetTop": "32px",
#         "height": "110px",
#         "borderWidth": "1px",
#         "borderColor": "#FF2B85FF",
#         "contents": [
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "width": "83px",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "สาเหตุที่ปิดร้านในเวลาทำการ",
#                 "weight": "bold",
#                 "size": "xs",
#                 "color": "#FF2B85FF",
#                 "align": "start",
#                 "gravity": "center",
#                 "wrap": true,
#                 "offsetStart": "3px",
#                 "offsetEnd": "3px",
#                 "contents": []
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "width": "80px",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "{top_offline_reason}",
#                 "size": "xs",
#                 "align": "center",
#                 "gravity": "center",
#                 "wrap": true,
#                 "offsetTop": "0px",
#                 "offsetStart": "2px",
#                 "offsetEnd": "2px",
#                 "contents": []
#               }
#             ]
#           },
#           {
#             "type": "box",
#             "layout": "horizontal",
#             "borderWidth": "1px",
#             "borderColor": "#FF2B85FF",
#             "contents": [
#               {
#                 "type": "text",
#                 "text": "{improve_top_offline_reason} คลิกที่นี่",
#                 "size": "xs",
#                 "align": "start",
#                 "gravity": "center",
#                 "wrap": true,
#                 "action": {
#                   "type": "uri",
#                   "label": "ที่นี่",
#                   "uri": "https://bit.ly/lineoffuni"
#                 },
#                 "offsetStart": "2px",
#                 "offsetEnd": "2px",
#                 "contents": [
#                   {
#                     "type": "span",
#                     "text": "{improve_top_offline_reason}"
#                   },
#                   {
#                     "type": "span",
#                     "text": "คลิก"
#                   },
#                   {
#                     "type": "span",
#                     "text": "ที่นี่",
#                     "color": "#FF2B85FF",
#                     "weight": "bold"
#                   }
#                 ]
#               }
#             ]
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "offsetTop": "35px",
#         "contents": [
#           {
#             "type": "text",
#             "text": "*รายงานผลประกอบการช่วงวันที่ {first_date} ถึง {last_date}",
#             "size": "xxs",
#             "align": "end",
#             "style": "italic",
#             "contents": []
#           }
#         ]
#       },
#       {
#         "type": "box",
#         "layout": "vertical",
#         "offsetTop": "40px",
#         "contents": [
#           {
#             "type": "text",
#             "text": "หากคุณต้องการแจ้งปัญหาเกี่ยวกับรายงานฉบับนี้ คลิกที่นี่",
#             "size": "xs",
#             "wrap": true,
#             "action": {
#               "type": "uri",
#               "label": "คลิกที่นี่",
#               "uri": "https://docs.google.com/forms/d/e/1FAIpQLScC8VpIJ2lDJQH6fYNN_s_cxfCtv43TCBLLAGbwaQa28-yYoQ/viewform"
#             },
#             "contents": [
#               {
#                 "type": "span",
#                 "text": "หากคุณต้องการ"
#               },
#               {
#                 "type": "span",
#                 "text": "แจ้งปัญหา",
#                 "color": "#FF2B85FF",
#                 "weight": "bold"
#               },
#               {
#                 "type": "span",
#                 "text": "เกี่ยวกับรายงานฉบับนี้ คลิก"
#               },
#               {
#                 "type": "span",
#                 "text": "ที่นี่",
#                 "color": "#FF2B85FF",
#                 "weight": "bold"
#               }
#             ]
#           }
#         ]
#       }
#     ]
#   }
# }
#     }
#   ]
# }
# """