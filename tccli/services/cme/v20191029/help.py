# -*- coding: utf-8 -*-
DESC = "cme-2019-10-29"
INFO = {
  "DescribeProjects": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "ProjectIds",
        "desc": "项目 Id 列表，N 从 0 开始取值，最大 19。"
      },
      {
        "name": "AspectRatioSet",
        "desc": "画布宽高比集合。"
      },
      {
        "name": "CategorySet",
        "desc": "项目类别集合。"
      },
      {
        "name": "Owner",
        "desc": "项目归属者。"
      },
      {
        "name": "Offset",
        "desc": "分页返回的起始偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "分页返回的记录条数，默认值：10。"
      }
    ],
    "desc": "支持根据多种条件过滤出项目列表。"
  },
  "ExportVideoEditProject": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 Id。"
      },
      {
        "name": "Definition",
        "desc": "导出模板 Id，目前不支持自定义创建，只支持下面的预置模板 Id。\n<li>10：分辨率为 480P，输出视频格式为 MP4；</li>\n<li>11：分辨率为 720P，输出视频格式为 MP4；</li>\n<li>12：分辨率为 1080P，输出视频格式为 MP4。</li>"
      },
      {
        "name": "ExportDestination",
        "desc": "导出目标。\n<li>CME：云剪，即导出为云剪素材；</li>\n<li>VOD：云点播，即导出为云点播媒资。</li>"
      },
      {
        "name": "CMEExportInfo",
        "desc": "导出的云剪素材信息。指定 ExportDestination = CME 时有效。"
      },
      {
        "name": "VODExportInfo",
        "desc": "导出的云点播媒资信息。指定 ExportDestination = VOD 时有效。"
      }
    ],
    "desc": "导出视频编辑项目，支持指定输出的模板。"
  },
  "ImportMediaToProject": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 Id。"
      },
      {
        "name": "VodFileId",
        "desc": "云点播媒资 FileId。"
      },
      {
        "name": "Name",
        "desc": "素材名称，不能超过30个字符。"
      },
      {
        "name": "PreProcessDefinition",
        "desc": "素材预处理任务模板 ID，取值：\n<li>10：进行编辑预处理。</li>\n注意：如果填0则不进行处理。"
      }
    ],
    "desc": "将云点播中的媒资添加到素材库中，提供给后续的视频编辑。"
  },
  "CreateProject": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "Category",
        "desc": "项目类别，取值有：\n<li>VIDEO_EDIT：视频编辑。</li>"
      },
      {
        "name": "Name",
        "desc": "项目名称，不可超过30个字符。"
      },
      {
        "name": "AspectRatio",
        "desc": "画布宽高比，取值有：\n<li>16:9；</li>\n<li>9:16。</li>"
      },
      {
        "name": "Owner",
        "desc": "归属者。"
      }
    ],
    "desc": "创建云剪的编辑项目，支持创建视频剪辑及直播剪辑两大类项目。\n"
  },
  "DeleteLoginStatus": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "UserIds",
        "desc": "用户 Id 列表，N 从 0 开始取值，最大 19。"
      }
    ],
    "desc": "删除用户登录态，使用户登出云剪平台。"
  },
  "DescribeTaskDetail": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "TaskId",
        "desc": "任务 Id。"
      }
    ],
    "desc": "获取任务详情信息，包含下面几个部分：\n<li>任务基础信息：包括任务状态、错误信息、创建时间等；</li>\n<li>导出项目输出信息：包括输出的素材 Id 等。</li>"
  },
  "DescribeLoginStatus": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "UserIds",
        "desc": "用户 Id 列表，N 从 0 开始取值，最大 19。"
      }
    ],
    "desc": "查询指定用户的登录态。"
  },
  "DeleteProject": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 Id。"
      }
    ],
    "desc": "删除云剪编辑项目。"
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 Id。"
      },
      {
        "name": "TaskTypeSet",
        "desc": "任务类型集合，取值有：\n<li>VIDEO_EDIT_PROJECT_EXPORT：视频编辑项目导出。</li>"
      },
      {
        "name": "StatusSet",
        "desc": "任务状态集合，取值有：\n<li>PROCESSING：处理中；</li>\n<li>SUCCESS：成功；</li>\n<li>FAIL：失败。</li>"
      },
      {
        "name": "Offset",
        "desc": "分页返回的起始偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "分页返回的记录条数，默认值：10。"
      }
    ],
    "desc": "支持各种条件筛选，返回对应的任务基础信息列表。"
  },
  "ModifyProject": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 Id。"
      },
      {
        "name": "Name",
        "desc": "项目名称，不可超过30个字符。"
      },
      {
        "name": "Owner",
        "desc": "归属者。"
      }
    ],
    "desc": "修改云剪编辑项目的信息。"
  }
}