# -*- coding: utf-8 -*-
DESC = "ticm-2018-11-27"
INFO = {
  "ImageModeration": {
    "params": [
      {
        "name": "Scenes",
        "desc": "本次调用支持的识别场景，可选值如下：\n1. PORN，即色情识别\n2. TERRORISM，即暴恐识别\n3. POLITICS，即政治敏感识别\n\n支持多场景（Scenes）一起检测。例如，使用 Scenes=[\"PORN\", \"TERRORISM\"]，即对一张图片同时进行色情识别和暴恐识别。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n • 图片格式：PNG、JPG、JPEG。 \n • 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n • 图片像素：大于50*50像素，否则影响识别效果； \n • 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "Config",
        "desc": "预留字段，后期用于展示更多识别信息。"
      },
      {
        "name": "Extra",
        "desc": "透传字段，透传简单信息。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      }
    ],
    "desc": "本接口提供多种维度的图像审核能力，支持色情和性感内容识别，政治人物和涉政敏感场景识别，以及暴恐人物、场景、旗帜标识等违禁内容的识别。"
  }
}