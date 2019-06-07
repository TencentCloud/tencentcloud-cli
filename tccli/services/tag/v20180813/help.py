# -*- coding: utf-8 -*-
DESC = "tag-2018-08-13"
INFO = {
  "UpdateResourceTagValue": {
    "params": [
      {
        "name": "TagKey",
        "desc": "资源关联的标签键"
      },
      {
        "name": "TagValue",
        "desc": "修改后的标签值"
      },
      {
        "name": "Resource",
        "desc": "资源的六段式描述"
      }
    ],
    "desc": "本接口用于修改资源已关联的标签值（标签键不变）"
  },
  "DescribeTagValues": {
    "params": [
      {
        "name": "TagKeys",
        "desc": "标签键列表"
      },
      {
        "name": "CreateUin",
        "desc": "创建者用户 Uin，不传或为空只将 Uin 作为条件查询"
      },
      {
        "name": "Offset",
        "desc": "数据偏移量，默认为 0, 必须为Limit参数的整数倍"
      },
      {
        "name": "Limit",
        "desc": "每页大小，默认为 15"
      }
    ],
    "desc": "用于查询已建立的标签列表中的标签值。"
  },
  "DescribeResourceTagsByResourceIds": {
    "params": [
      {
        "name": "ServiceType",
        "desc": "业务类型"
      },
      {
        "name": "ResourcePrefix",
        "desc": "资源前缀"
      },
      {
        "name": "ResourceIds",
        "desc": "资源唯一标记"
      },
      {
        "name": "ResourceRegion",
        "desc": "资源所在地域"
      },
      {
        "name": "Offset",
        "desc": "数据偏移量，默认为 0, 必须为Limit参数的整数倍"
      },
      {
        "name": "Limit",
        "desc": "每页大小，默认为 15"
      }
    ],
    "desc": "用于查询已有资源标签键值对"
  },
  "DescribeTagKeys": {
    "params": [
      {
        "name": "CreateUin",
        "desc": "创建者用户 Uin，不传或为空只将 Uin 作为条件查询"
      },
      {
        "name": "Offset",
        "desc": "数据偏移量，默认为 0, 必须为Limit参数的整数倍"
      },
      {
        "name": "Limit",
        "desc": "每页大小，默认为 15"
      }
    ],
    "desc": "用于查询已建立的标签列表中的标签键。\n"
  },
  "DeleteResourceTag": {
    "params": [
      {
        "name": "TagKey",
        "desc": "标签键"
      },
      {
        "name": "Resource",
        "desc": "资源六段式描述"
      }
    ],
    "desc": "本接口用于解除标签和资源的关联关系"
  },
  "DescribeTags": {
    "params": [
      {
        "name": "TagKey",
        "desc": "标签键,与标签值同时存在或同时不存在，不存在时表示查询该用户所有标签"
      },
      {
        "name": "TagValue",
        "desc": "标签值,与标签键同时存在或同时不存在，不存在时表示查询该用户所有标签"
      },
      {
        "name": "Offset",
        "desc": "数据偏移量，默认为 0, 必须为Limit参数的整数倍"
      },
      {
        "name": "Limit",
        "desc": "每页大小，默认为 15"
      },
      {
        "name": "CreateUin",
        "desc": "创建者用户 Uin，不传或为空只将 Uin 作为条件查询"
      }
    ],
    "desc": "用于查询已建立的标签列表。\n"
  },
  "ModifyResourceTags": {
    "params": [
      {
        "name": "Resource",
        "desc": "资源的六段式描述"
      },
      {
        "name": "ReplaceTags",
        "desc": "需要增加或修改的标签集合。如果Resource描述的资源未关联输入的标签键，则增加关联；若已关联，则将该资源关联的键对应的标签值修改为输入值。本接口中ReplaceTags和DeleteTags二者必须存在其一，且二者不能包含相同的标签键"
      },
      {
        "name": "DeleteTags",
        "desc": "需要解关联的标签集合。本接口中ReplaceTags和DeleteTags二者必须存在其一，且二者不能包含相同的标签键"
      }
    ],
    "desc": "本接口用于修改资源关联的所有标签"
  },
  "AddResourceTag": {
    "params": [
      {
        "name": "TagKey",
        "desc": "标签键"
      },
      {
        "name": "TagValue",
        "desc": "标签值"
      },
      {
        "name": "Resource",
        "desc": "资源六段式描述"
      }
    ],
    "desc": "本接口用于给标签关联资源"
  },
  "DeleteTag": {
    "params": [
      {
        "name": "TagKey",
        "desc": "需要删除的标签键"
      },
      {
        "name": "TagValue",
        "desc": "需要删除的标签值"
      }
    ],
    "desc": "本接口用于删除一对标签键和标签值"
  },
  "CreateTag": {
    "params": [
      {
        "name": "TagKey",
        "desc": "标签键"
      },
      {
        "name": "TagValue",
        "desc": "标签值"
      }
    ],
    "desc": "本接口用于创建一对标签键和标签值"
  }
}