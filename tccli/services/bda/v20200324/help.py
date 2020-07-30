# -*- coding: utf-8 -*-
DESC = "bda-2020-03-24"
INFO = {
  "SearchTrace": {
    "params": [
      {
        "name": "GroupId",
        "desc": "希望搜索的人体库ID。"
      },
      {
        "name": "Trace",
        "desc": "人体轨迹信息。"
      },
      {
        "name": "MaxPersonNum",
        "desc": "单张被识别的人体轨迹返回的最相似人员数量。\n默认值为5，最大值为100。\n 例，设MaxPersonNum为8，则返回Top8相似的人员信息。 值越大，需要处理的时间越长。建议不要超过10。"
      },
      {
        "name": "TraceMatchThreshold",
        "desc": "出参Score中，只有超过TraceMatchThreshold值的结果才会返回。\n默认为0。范围[0, 100.0]。"
      }
    ],
    "desc": "本接口用于对一组待识别的人体轨迹（Trace）图片，在人体库中识别出最相似的 TopK 人体，按照相似度从大到小排列。\n\n人体轨迹（Trace）图片要求：图片中当且仅包含一个人体。人体完整、无遮挡。\n\n> 请注意：\n- 我们希望您的输入为严格符合轨迹图片要求的图片。如果您输入的图片不符合轨迹图片要求，会对最终效果产生较大负面影响；\n- 人体轨迹，是一个包含1-5张图片的图片序列。您可以输入1张图片作为轨迹，也可以输入多张。单个轨迹中包含越多符合质量的图片，搜索效果越好。\n- 构成人体轨迹单张图片大小不得超过2M，分辨率不得超过1920*1080。"
  },
  "DetectBody": {
    "params": [
      {
        "name": "Image",
        "desc": "人体图片 Base64 数据。\n图片 base64 编码后大小不可超过5M。\n图片分辨率不得超过 2048*2048。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "人体图片 Url 。\nUrl、Image必须提供一个，如果都提供，只使用 Url。\n图片 base64 编码后大小不可超过5M。 \n图片分辨率不得超过 2048*2048。\n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "MaxBodyNum",
        "desc": "最多检测的人体数目，默认值为1（仅检测图片中面积最大的那个人体）； 最大值10 ，检测图片中面积最大的10个人体。"
      },
      {
        "name": "AttributesOptions",
        "desc": "是否返回年龄、性别、朝向等属性。 \n可选项有 Age、Bag、Gender、UpperBodyCloth、LowerBodyCloth、Orientation。  \n如果此参数为空则为不需要返回。 \n需要将属性组成一个用逗号分隔的字符串，属性之间的顺序没有要求。 \n关于各属性的详细描述，参见下文出参。 \n最多返回面积最大的 5 个人体属性信息，超过 5 个人体（第 6 个及以后的人体）的 BodyAttributesInfo 不具备参考意义。"
      }
    ],
    "desc": "检测给定图片中的人体（Body）的位置信息及属性信息。\n"
  },
  "SegmentPortraitPic": {
    "params": [
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n图片分辨率须小于2000*2000。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。\nUrl、Image必须提供一个，如果都提供，只使用 Url。\n图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  \n非腾讯云存储的Url速度和稳定性可能受一定影响。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      }
    ],
    "desc": "识别传入图片中人体的完整轮廓，进行抠像。\n"
  },
  "DetectBodyJoints": {
    "params": [
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。  \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。 \nUrl、Image必须提供一个，如果都提供，只使用 Url。  \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。  \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      }
    ],
    "desc": "检测图片中人体的14个关键点。建议用于人体图像清晰、无遮挡的场景。支持一张图片中存在多个人体的识别。\n"
  },
  "CreateTrace": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员ID。"
      },
      {
        "name": "Trace",
        "desc": "人体轨迹信息。"
      }
    ],
    "desc": "将一个人体轨迹添加到一个人员中。一个人员最多允许包含 5 个人体轨迹。同一人的人体轨迹越多，搜索识别效果越好。\n\n>请注意：\n- 我们希望您的输入为 严格符合轨迹图片 要求的图片。如果您输入的图片不符合轨迹图片要求，会对最终效果产生较大负面影响。请您尽量保证一个Trace中的图片人体清晰、无遮挡、连贯。\n- 一个人体轨迹（Trace）可以包含1-5张人体图片。提供越多质量高的人体图片有助于提升最终识别结果。\n- 无论您在单个Trace中提供了多少张人体图片，我们都将生成一个对应的轨迹（Trace）信息。即，Trace仅和本次输入的图片序列相关，和图片的个数无关。\n- 输入的图片组中，若有部分图片输入不合法（如图片大小过大、分辨率过大、无法解码等），我们将舍弃这部分图片，确保合法图片被正确搜索。即，我们将尽可能保证请求成功，去除不合法的输入；\n- 构成人体轨迹单张图片大小限制为2M，分辨率限制为1920*1080。"
  },
  "DeleteGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "人体库ID。"
      }
    ],
    "desc": "删除该人体库及包含的所有的人员。"
  },
  "DeletePerson": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员ID。"
      }
    ],
    "desc": "删除人员。"
  },
  "SegmentCustomizedPortraitPic": {
    "params": [
      {
        "name": "SegmentationOptions",
        "desc": "此参数为分割选项，请根据需要选择自己所想从图片中分割的部分。注意所有选项均为非必选，如未选择则值默认为false, 但是必须要保证多于一个选项的描述为true。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n图片分辨率须小于2000*2000。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。\nUrl、Image必须提供一个，如果都提供，只使用 Url。\n图片分辨率须小于2000*2000 ，图片 base64 编码后大小不可超过5M。 \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  \n非腾讯云存储的Url速度和稳定性可能受一定影响。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      }
    ],
    "desc": "在前后景分割的基础上优化多分类分割，支持对头发、五官等的分割，既作为换发型、挂件等底层技术，也可用于扣人头、扣人脸等玩法"
  },
  "ModifyGroup": {
    "params": [
      {
        "name": "GroupId",
        "desc": "人体库ID。"
      },
      {
        "name": "GroupName",
        "desc": "人体库名称。"
      },
      {
        "name": "Tag",
        "desc": "人体库信息备注。"
      }
    ],
    "desc": "修改人体库名称、备注。"
  },
  "GetGroupList": {
    "params": [
      {
        "name": "Offset",
        "desc": "起始序号，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认值为10，最大值为1000。"
      }
    ],
    "desc": "获取人体库列表。"
  },
  "CreateGroup": {
    "params": [
      {
        "name": "GroupName",
        "desc": "人体库名称，[1,60]个字符，可修改，不可重复。"
      },
      {
        "name": "GroupId",
        "desc": "人体库 ID，不可修改，不可重复。支持英文、数字、-%@#&_，长度限制64B。"
      },
      {
        "name": "Tag",
        "desc": "人体库信息备注，[0，40]个字符。"
      },
      {
        "name": "BodyModelVersion",
        "desc": "人体识别所用的算法模型版本。 \n目前入参仅支持 “1.0”1个输入。 默认为\"1.0\"。  \n不同算法模型版本对应的人体识别算法不同，新版本的整体效果会优于旧版本，后续我们将推出更新版本。"
      }
    ],
    "desc": "用于创建一个空的人体库，如果人体库已存在返回错误。\n\n1个APPID下最多有2000W个人体轨迹（Trace），最多1W个人体库（Group）。\n\n单个人体库（Group）最多10W个人体轨迹（Trace）。\n\n单个人员（Person）最多添加 5 个人体轨迹（Trace）。"
  },
  "CreatePerson": {
    "params": [
      {
        "name": "GroupId",
        "desc": "待加入的人员库ID。"
      },
      {
        "name": "PersonName",
        "desc": "人员名称。[1，60]个字符，可修改，可重复。"
      },
      {
        "name": "PersonId",
        "desc": "人员ID，单个腾讯云账号下不可修改，不可重复。 \n支持英文、数字、-%@#&_，，长度限制64B。"
      },
      {
        "name": "Trace",
        "desc": "人体轨迹信息。"
      }
    ],
    "desc": "创建人员，添加对应人员的人体轨迹信息。\n\n请注意：\n- 我们希望您的输入为 严格符合轨迹图片 要求的图片。如果您输入的图片不符合轨迹图片要求，会对最终效果产生较大负面影响。请您尽量保证一个Trace中的图片人体清晰、无遮挡、连贯；\n- 一个人体轨迹（Trace）可以包含1-5张人体图片。提供越多质量高的人体图片有助于提升最终识别结果；\n- 无论您在单个Trace中提供了多少张人体图片，我们都将生成一个对应的轨迹（Trace）信息。即，Trace仅和本次输入的图片序列相关，和图片的个数无关；\n- 输入的图片组中，若有部分图片输入不合法（如图片大小过大、分辨率过大、无法解码等），我们将舍弃这部分图片，确保合法图片被正确搜索。即，我们将尽可能保证请求成功，去除不合法的输入；\n- 构成人体轨迹单张图片大小不得超过2M，分辨率不得超过1920*1080。"
  },
  "GetPersonList": {
    "params": [
      {
        "name": "GroupId",
        "desc": "人体库ID。"
      },
      {
        "name": "Offset",
        "desc": "起始序号，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认值为10，最大值为1000。"
      }
    ],
    "desc": "获取指定人体库中的人员列表。"
  },
  "ModifyPersonInfo": {
    "params": [
      {
        "name": "PersonId",
        "desc": "人员ID。"
      },
      {
        "name": "PersonName",
        "desc": "人员名称。"
      }
    ],
    "desc": "修改人员信息。"
  }
}