# -*- coding: utf-8 -*-
DESC = "tmt-2018-03-21"
INFO = {
  "TextTranslate": {
    "params": [
      {
        "name": "SourceText",
        "desc": "待翻译的文本"
      },
      {
        "name": "Source",
        "desc": "源语言，参照Target支持语言列表"
      },
      {
        "name": "Target",
        "desc": "目标语言，参照支持语言列表\n<li> zh : 中文 </li> <li> en : 英文 </li><li> jp : 日语 </li> <li> kr : 韩语 </li><li> de : 德语 </li><li> fr : 法语 </li><li> es : 西班牙文 </li> <li> it : 意大利文 </li><li> tr : 土耳其文 </li><li> ru : 俄文 </li><li> pt : 葡萄牙文 </li><li> vi : 越南文 </li><li> id : 印度尼西亚文 </li><li> ms : 马来西亚文 </li><li> th : 泰文 </li><li> auto : 自动识别源语言，只能用于source字段 </li>"
      },
      {
        "name": "ProjectId",
        "desc": "项目id"
      }
    ],
    "desc": "提供中文到英文、英文到中文的等多种语言的文本内容翻译服务， 经过大数据语料库、多种解码算法、翻译引擎深度优化，在新闻文章、生活口语等不同语言场景中都有深厚积累，翻译结果专业评价处于行业顶级水平。\n"
  },
  "ImageTranslate": {
    "params": [
      {
        "name": "SessionUuid",
        "desc": "唯一id，返回时原样返回"
      },
      {
        "name": "Scene",
        "desc": "doc:文档扫描"
      },
      {
        "name": "Data",
        "desc": "图片数据的Base64字符串"
      },
      {
        "name": "Source",
        "desc": "源语言，支持语言列表<li> zh : 中文 </li> <li> en : 英文 </li>"
      },
      {
        "name": "Target",
        "desc": "目标语言，支持语言列表<li> zh : 中文 </li> <li> en : 英文 </li>"
      },
      {
        "name": "ProjectId",
        "desc": "项目id"
      }
    ],
    "desc": "提供中文到英文、英文到中文两种语言的图片翻译服务，可自动识别图片中的文本内容并翻译成目标语言"
  },
  "SpeechTranslate": {
    "params": [
      {
        "name": "SessionUuid",
        "desc": "一段完整的语音对应一个SessionUuid"
      },
      {
        "name": "Source",
        "desc": "音频中的语言类型，支持语言列表<li> zh : 中文 </li> <li> en : 英文 </li>"
      },
      {
        "name": "Target",
        "desc": "翻译目标语⾔言类型 ，支持的语言列表<li> zh : 中文 </li> <li> en : 英文 </li>"
      },
      {
        "name": "AudioFormat",
        "desc": "pcm : 146   amr : 33554432   mp3 : 83886080"
      },
      {
        "name": "Seq",
        "desc": "语音分片后的第几片"
      },
      {
        "name": "IsEnd",
        "desc": "是否最后一片"
      },
      {
        "name": "Data",
        "desc": "语音分片内容的base64字符串"
      },
      {
        "name": "ProjectId",
        "desc": "项目id"
      }
    ],
    "desc": "本接口提供音频内文字识别 + 翻译功能，目前开放中到英的语音翻译服务。\n待识别和翻译的音频文件可以是 pcm、mp3、amr和speex 格式，音频内语音清晰，采用流式传输和翻译的方式。\n"
  },
  "LanguageDetect": {
    "params": [
      {
        "name": "Text",
        "desc": "待识别的文本"
      },
      {
        "name": "ProjectId",
        "desc": "项目id"
      }
    ],
    "desc": "可自动识别文本内容的语言种类，轻量高效，无需额外实现判断方式，使面向客户的服务体验更佳。"
  }
}