# -*- coding: utf-8 -*-
DESC = "cme-2019-10-29"
INFO = {
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
    "desc": "获取任务列表，支持条件筛选，返回对应的任务基础信息列表。"
  },
  "DescribeTeams": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "TeamIds",
        "desc": "团队 ID 列表，限30个。"
      }
    ],
    "desc": "获取指定团队的信息。"
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
  "DescribeSharedSpace": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "Authorizee",
        "desc": "被授权目标实体。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "获取共享空间。当实体A对实体B授权某资源以后，实体B的共享空间就会增加实体A。"
  },
  "GrantResourceAuthorization": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "Owner",
        "desc": "资源所属实体。"
      },
      {
        "name": "Resources",
        "desc": "被授权资源。"
      },
      {
        "name": "Authorizees",
        "desc": "被授权目标实体。"
      },
      {
        "name": "Permissions",
        "desc": "详细授权值。 取值有：\n<li>R：可读，可以浏览素材，但不能使用该素材（将其添加到 Project），或复制到自己的媒资库中</li>\n<li>X：可用，可以使用该素材（将其添加到 Project），但不能将其复制到自己的媒资库中，意味着被授权者无法将该资源进一步扩散给其他个人或团队。</li>\n<li>C：可复制，既可以使用该素材（将其添加到 Project），也可以将其复制到自己的媒资库中。</li>\n<li>W：可修改、删除媒资。</li>"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "资源所属实体对目标实体授予目标资源的相应权限。"
  },
  "SearchMaterial": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "SearchScopes",
        "desc": "指定搜索空间，数组长度不得超过5。"
      },
      {
        "name": "MaterialTypes",
        "desc": "素材类型，取值：\n<li>AUDIO：音频；</li>\n<li>VIDEO：视频 ；</li>\n<li>IMAGE：图片。</li>"
      },
      {
        "name": "Text",
        "desc": "搜索文本，模糊匹配素材名称或描述信息，匹配项越多，匹配度越高，排序越优先。长度限制：15个字符。"
      },
      {
        "name": "Resolution",
        "desc": "按画质检索，取值为：LD/SD/HD/FHD/2K/4K。"
      },
      {
        "name": "DurationRange",
        "desc": "按素材时长检索，单位s。"
      },
      {
        "name": "CreateTimeRange",
        "desc": "按照素材创建时间检索。"
      },
      {
        "name": "Tags",
        "desc": "按标签检索，填入检索的标签名。"
      },
      {
        "name": "Sort",
        "desc": "排序方式。Sort.Field 可选值：CreateTime。指定 Text 搜索时，将根据匹配度排序，该字段无效。"
      },
      {
        "name": "Offset",
        "desc": "偏移量。默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：50。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "根据检索条件搜索素材，返回素材的基本信息。"
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
  "DescribeJoinTeams": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "MemberId",
        "desc": "团队成员　ID。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：30，最大值：30。"
      }
    ],
    "desc": "获取指定的团队成员所加入的团队列表。"
  },
  "DescribeResourceAuthorization": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "Owner",
        "desc": "归属者。"
      },
      {
        "name": "Resource",
        "desc": "资源。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "查询指定资源的授权列表。"
  },
  "ImportMaterial": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "VodFileId",
        "desc": "云点播媒资 FileId。"
      },
      {
        "name": "Owner",
        "desc": "素材归属者。"
      },
      {
        "name": "Name",
        "desc": "素材名称，不能超过30个字符。"
      },
      {
        "name": "ClassPath",
        "desc": "素材分类路径，形如：\"/a/b\"，层级数不能超过10，每个层级长度不能超过15字符。若不填则默认为根路径。"
      },
      {
        "name": "PreProcessDefinition",
        "desc": "素材预处理任务模板 ID。取值：\n<li>10：进行编辑预处理。</li>"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "将云点播媒资文件导入到云剪素材库。"
  },
  "ExportVideoByEditorTrackData": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
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
        "name": "TrackData",
        "desc": "在线编辑轨道数据。"
      },
      {
        "name": "CMEExportInfo",
        "desc": "导出的云剪素材信息。指定 ExportDestination = CME 时有效。"
      },
      {
        "name": "VODExportInfo",
        "desc": "导出的云点播媒资信息。指定 ExportDestination = VOD 时有效。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "使用在线编辑轨道数据直接导出视频。"
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
  "CreateLink": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "Type",
        "desc": "链接类型，取值有:\n<li>CLASS: 分类链接；</li>\n<li> MATERIAL：素材链接。</li>"
      },
      {
        "name": "Name",
        "desc": "链接名称，不能超过30个字符。"
      },
      {
        "name": "Owner",
        "desc": "链接归属实体。"
      },
      {
        "name": "DestinationId",
        "desc": "目标资源Id。取值：\n<li>当 Type 为 MATERIAL 时填素材 ID；</li>\n<li>当 Type 为 CLASS 时填写分类路径。</li>"
      },
      {
        "name": "DestinationOwner",
        "desc": "目标资源归属者。"
      },
      {
        "name": "ClassPath",
        "desc": "链接的分类路径，如填\"/a/b\"则代表链接属于该分类路径，不填则默认为根路径。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": " 创建素材链接或分类路径链接，将源资源信息链接到目标。"
  },
  "ModifyTeam": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "TeamId",
        "desc": "团队 ID。"
      },
      {
        "name": "Name",
        "desc": "团队名称，不能超过 30 个字符。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "修改团队信息，目前支持修改的操作有：\n<li>修改团队名称。</li>"
  },
  "DeleteMaterial": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "MaterialId",
        "desc": "素材 Id。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "根据素材 Id 删除素材。"
  },
  "CreateClass": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "Owner",
        "desc": "归属者。"
      },
      {
        "name": "ClassPath",
        "desc": "分类路径。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "新增分类，用于管理素材。\n<li>分类层数不能超过10；</li>\n<li>子分类数不能超过10。</li>"
  },
  "DeleteTeam": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问平台。"
      },
      {
        "name": "TeamId",
        "desc": "要删除的团队  ID。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "删除一个团队。\n<li>要删除的团队必须没有归属的素材；</li>\n<li>要删除的团队必须没有归属的分类。</li>"
  },
  "AddTeamMember": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "TeamId",
        "desc": "团队 ID。"
      },
      {
        "name": "TeamMembers",
        "desc": "要添加的成员列表，一次最多添加30个成员。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "向一个团队中团队成员，并且指定成员的角色。"
  },
  "MoveClass": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "Owner",
        "desc": "归属者。"
      },
      {
        "name": "SourceClassPath",
        "desc": "源分类路径。"
      },
      {
        "name": "DestinationClassPath",
        "desc": "目标分类路径。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "移动某一个分类到另外一个分类下，也可用于分类重命名。\n<li>如果 SourceClassPath = /素材/视频/NBA，DestinationClassPath = /素材/视频/篮球，当 DestinationClassPath 不存在时候，操作结果为重命名 ClassPath，如果 DestinationClassPath 存在时候，操作结果为产生新目录 /素材/视频/篮球/NBA。</li>"
  },
  "ModifyTeamMember": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "TeamId",
        "desc": "团队 ID。"
      },
      {
        "name": "MemberId",
        "desc": "团队成员 ID。"
      },
      {
        "name": "Remark",
        "desc": "成员备注，允许设置备注为空，不为空时长度不能超过15个字符。"
      },
      {
        "name": "Role",
        "desc": "成员角色，取值：\n<li>Admin：团队管理员；</li>\n<li>Member：普通成员。</li>"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "修改团队成员信息，包括成员备注、角色等。"
  },
  "DeleteTeamMembers": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "TeamId",
        "desc": "团队 ID。"
      },
      {
        "name": "MemberIds",
        "desc": "要删除的成员列表。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "将团队成员从团队中删除，默认只有 Owner 及管理员才有此权限。"
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
        "name": "Sort",
        "desc": "列表排序，支持下列排序字段：\n<li>CreateTime：创建时间；</li>\n<li>UpdateTime：更新时间。</li>"
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
  "DescribeMaterials": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "MaterialIds",
        "desc": "素材 ID 列表，N 从 0 开始取值，最大 19。"
      },
      {
        "name": "Sort",
        "desc": "列表排序，支持下列排序字段：\n<li>CreateTime：创建时间；</li>\n<li>UpdateTime：更新时间。</li>"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "根据素材 Id 批量获取素材详情。"
  },
  "DescribeClass": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "Owner",
        "desc": "归属者。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "获取指定归属者下所有的分类信息。"
  },
  "CreateTeam": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "Name",
        "desc": "团队名称，限30个字符。"
      },
      {
        "name": "OwnerId",
        "desc": "团队所有者，指定用户 ID。"
      },
      {
        "name": "OwnerRemark",
        "desc": "团队所有者的备注，限30个字符。"
      },
      {
        "name": "TeamId",
        "desc": "自定义团队 ID。创建后不可修改，限20个英文字符及\"-\"。同时不能以 cmetid_开头。不填会生成默认团队 ID。"
      }
    ],
    "desc": "创建一个团队。"
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
        "name": "AspectRatio",
        "desc": "画布宽高比，取值有：\n<li>16:9；</li>\n<li>9:16。</li>"
      },
      {
        "name": "Owner",
        "desc": "归属者。"
      }
    ],
    "desc": "修改云剪编辑项目的信息。"
  },
  "ModifyMaterial": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "MaterialId",
        "desc": "素材 Id。"
      },
      {
        "name": "Owner",
        "desc": "素材归属。"
      },
      {
        "name": "Name",
        "desc": "素材名称，不能超过30个字符。"
      },
      {
        "name": "ClassPath",
        "desc": "素材分类路径，例如填写\"/a/b\"，则代表该素材存储的路径为\"/a/b\"。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "修改素材信息，支持修改素材名称、分类路径、标签等信息。"
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
    "desc": "将云点播中的媒资添加到素材库中，供后续视频编辑使用。"
  },
  "ListMedia": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "ClassPath",
        "desc": "素材分类路径，例如填写\"/a/b\"，则代表浏览该分类路径下的素材和子分类信息。"
      },
      {
        "name": "Owner",
        "desc": "素材和分类的归属者。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：50。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": " 浏览当前分类路径下的资源，包括素材和子分类。"
  },
  "RevokeResourceAuthorization": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "Owner",
        "desc": "资源所属实体。"
      },
      {
        "name": "Resources",
        "desc": "被授权资源。"
      },
      {
        "name": "Authorizees",
        "desc": "被授权目标实体。"
      },
      {
        "name": "Permissions",
        "desc": "详细授权值。 取值有：\n<li>R：可读，可以浏览素材，但不能使用该素材（将其添加到 Project），或复制到自己的媒资库中</li>\n<li>X：可用，可以使用该素材（将其添加到 Project），但不能将其复制到自己的媒资库中，意味着被授权者无法将该资源进一步扩散给其他个人或团队。</li>\n<li>C：可复制，既可以使用该素材（将其添加到 Project），也可以将其复制到自己的媒资库中。</li>\n<li>W：可修改、删除媒资。</li>"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": " 资源所属实体对目标实体回收目标资源的相应权限，若原本没有相应权限则不产生变更。"
  },
  "DeleteClass": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "Owner",
        "desc": "归属者。"
      },
      {
        "name": "ClassPath",
        "desc": "分类路径。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "删除分类信息，删除时检验下述限制：\n<li>分类路径必须存在；</li>\n<li>分类下没有绑定素材。</li>"
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
  "FlattenListMedia": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "ClassPath",
        "desc": "素材分类路径，例如填写\"/a/b\"，则代表平铺该分类路径下及其子分类路径下的素材信息。"
      },
      {
        "name": "Owner",
        "desc": "素材路径的归属者。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0。"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：10，最大值：50。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "平铺分类路径下及其子分类下的所有素材。"
  },
  "DescribeTeamMembers": {
    "params": [
      {
        "name": "Platform",
        "desc": "平台名称，指定访问的平台。"
      },
      {
        "name": "TeamId",
        "desc": "团队 ID。"
      },
      {
        "name": "MemberIds",
        "desc": "成员 ID 列表，限指定30个指定成员。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量，默认值：0"
      },
      {
        "name": "Limit",
        "desc": "返回记录条数，默认值：30，最大值：30。"
      },
      {
        "name": "Operator",
        "desc": "操作者。填写用户的 Id，用于标识调用者及校验操作权限。"
      }
    ],
    "desc": "获取指定成员 ID 的信息，同时支持拉取所有团队成员信息。"
  }
}