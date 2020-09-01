# -*- coding: utf-8 -*-
DESC = "ft-2020-03-04"
INFO = {
  "CancelFaceMorphJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "人像渐变任务Job id"
      }
    ],
    "desc": "撤销人像渐变任务请求"
  },
  "SwapGenderPic": {
    "params": [
      {
        "name": "GenderInfos",
        "desc": "人脸转化性别信息。 \n您可以输入最多3个 GenderInfo 来实现给一张图中的最多3张人脸转换性别。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url ，对应图片 base64 编码后大小不可超过5M。 \n图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 \n图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "RspImgType",
        "desc": "返回图像方式（base64 或 url ) ，二选一。url有效期为1天。"
      }
    ],
    "desc": "用户上传一张人脸图片，基于人脸编辑与生成算法，输出一张人脸性别转换的图片。男变女可实现美颜、淡妆、加刘海和长发的效果；女变男可实现加胡须、变短发的效果。 "
  },
  "MorphFace": {
    "params": [
      {
        "name": "Images",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。 \njpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。 \n人员人脸总数量至少2张，不可超过5张。 \n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Urls",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。jpg格式长边像素不可超过4000，其他格式图片长边像素不可超2000。 \nUrl、Image必须提供一个，如果都提供，只使用 Url。图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。 \n人员人脸总数量不可超过5张。 \n若图片中包含多张人脸，只选取其中人脸面积最大的人脸。"
      },
      {
        "name": "GradientInfos",
        "desc": "人脸渐变参数。可调整每张图片的展示时长、人像渐变的最长时间"
      },
      {
        "name": "Fps",
        "desc": "视频帧率，取值[1,60]。默认10"
      },
      {
        "name": "OutputType",
        "desc": "视频类型，取值[0,2]，其中0为MP4，1为GIF，2为MOV。目前仅支持MP4格式，默认为MP4格式"
      },
      {
        "name": "OutputWidth",
        "desc": "视频宽度，取值[128,1280]。默认值720"
      },
      {
        "name": "OutputHeight",
        "desc": "视频高度，取值[128,1280]。默认值1280"
      }
    ],
    "desc": "输入2-5张人脸照片，生成一段以人脸为焦点的渐变视频或GIF图，支持自定义图片播放速度、视频每秒传输帧数，可用于短视频、表情包、创意H5等应用场景，丰富静态图片的玩法。"
  },
  "ChangeAgePic": {
    "params": [
      {
        "name": "AgeInfos",
        "desc": "人脸变老变年轻信息。 \n您可以输入最多3个 AgeInfo 来实现给一张图中的最多3张人脸变老变年轻。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url ，对应图片 base64 编码后大小不可超过5M。 \n图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 \n图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "RspImgType",
        "desc": "返回图像方式（base64 或 url ) ，二选一。url有效期为1天。"
      }
    ],
    "desc": "用户上传一张人脸图片，基于人脸编辑与生成算法，输出一张人脸变老或变年轻的图片，支持实现人脸不同年龄的变化。"
  },
  "QueryFaceMorphJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "人像渐变任务Job id"
      }
    ],
    "desc": "查询人像渐变处理进度"
  },
  "FaceCartoonPic": {
    "params": [
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url ，对应图片 base64 编码后大小不可超过5M。\n图片的 Url、Image必须提供一个，如果都提供，只使用 Url。\n图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。\n非腾讯云存储的Url速度和稳定性可能受一定影响。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "RspImgType",
        "desc": "返回图像方式（base64 或 url ) ，二选一。url有效期为1天。"
      },
      {
        "name": "DisableGlobalEffect",
        "desc": "是否取消全图动漫化效果。"
      }
    ],
    "desc": "输入一张人脸照片，生成个性化的二次元动漫形象，可用于打造个性头像、趣味活动、特效类应用等场景，提升社交娱乐的体验。"
  }
}