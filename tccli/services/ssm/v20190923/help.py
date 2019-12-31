# -*- coding: utf-8 -*-
DESC = "ssm-2019-09-23"
INFO = {
  "PutSecretValue": {
    "params": [
      {
        "name": "SecretName",
        "desc": "指定需要增加版本的凭据名称。"
      },
      {
        "name": "VersionId",
        "desc": "指定新增加的版本号，最长64 字节，使用字母、数字或者 - _ . 的组合并且以字母或数字开头。"
      },
      {
        "name": "SecretBinary",
        "desc": "二进制凭据信息，使用base64编码。SecretBinary 和 SecretString 必须且只能设置一个。"
      },
      {
        "name": "SecretString",
        "desc": "文本类型凭据信息明文（不需要进行base64编码），SecretBinary 和 SecretString 必须且只能设置一个。"
      }
    ],
    "desc": "该接口在指定名称的凭据下增加新版本的凭据内容，一个凭据下最多可以支持10个版本。只能对处于Enabled 和 Disabled 状态的凭据添加新的版本。"
  },
  "ListSecretVersionIds": {
    "params": [
      {
        "name": "SecretName",
        "desc": "凭据名称。"
      }
    ],
    "desc": "该接口用于获取指定凭据下的版本列表信息"
  },
  "RestoreSecret": {
    "params": [
      {
        "name": "SecretName",
        "desc": "指定需要恢复的凭据名称。"
      }
    ],
    "desc": "该接口用于恢复计划删除（PendingDelete状态）中的凭据，取消计划删除。取消计划删除的凭据将处于Disabled 状态，如需恢复使用，通过EnableSecret 接口开启凭据。"
  },
  "CreateSecret": {
    "params": [
      {
        "name": "SecretName",
        "desc": "凭据名称，同一region内不可重复，最长128字节，使用字母、数字或者 - _ 的组合，第一个字符必须为字母或者数字。"
      },
      {
        "name": "VersionId",
        "desc": "凭据版本，查询凭据信息时需要根据SecretName 和 VersionId进行查询，最长64 字节，使用字母、数字或者 - _ . 的组合并且以字母或数字开头。"
      },
      {
        "name": "Description",
        "desc": "描述信息，用于详细描述用途等，最大支持2048字节。"
      },
      {
        "name": "KmsKeyId",
        "desc": "指定对凭据进行加密的KMS CMK。如果为空则表示使用Secrets Manager为您默认创建的CMK进行加密。您也可以指定在同region 下自行创建的KMS CMK进行加密。"
      },
      {
        "name": "SecretBinary",
        "desc": "二进制凭据信息base64编码后的明文。SecretBinary 和 SecretString 必须且只能设置一个，最大支持4096字节。"
      },
      {
        "name": "SecretString",
        "desc": "文本类型凭据信息明文（不需要进行base64编码）。SecretBinary 和 SecretString 必须且只能设置一个，，最大支持4096字节。"
      }
    ],
    "desc": "创建新的凭据信息，通过KMS进行加密保护。每个Region最多可创建存储1000个凭据信息。"
  },
  "DeleteSecret": {
    "params": [
      {
        "name": "SecretName",
        "desc": "指定需要删除的凭据名称。"
      },
      {
        "name": "RecoveryWindowInDays",
        "desc": "指定计划删除日期，单位（天），0（默认）表示立即删除， 1-30 表示预留的天数，超出该日期之后彻底删除。"
      }
    ],
    "desc": "删除指定的凭据信息，可以通过RecoveryWindowInDays参数设置立即删除或者计划删除。对于计划删除的凭据，在删除日期到达之前状态为 PendingDelete，并可以通过RestoreSecret 进行恢复，超出指定删除日期之后会被彻底删除。您必须先通过 DisableSecret 停用凭据后才可以进行（计划）删除操作。"
  },
  "EnableSecret": {
    "params": [
      {
        "name": "SecretName",
        "desc": "指定启用凭据的名称。"
      }
    ],
    "desc": "该接口用于开启凭据，状态为Enabled。可以通过 GetSecretValue 接口获取凭据明文。处于PendingDelete状态的凭据不能直接开启，需要通过RestoreSecret 恢复后再开启使用。"
  },
  "UpdateSecret": {
    "params": [
      {
        "name": "SecretName",
        "desc": "指定需要更新凭据内容的名称。"
      },
      {
        "name": "VersionId",
        "desc": "指定需要更新凭据内容的版本号。"
      },
      {
        "name": "SecretBinary",
        "desc": "新的凭据内容为二进制的场景使用该字段，并使用base64进行编码。SecretBinary 和 SecretString 只能一个不为空。"
      },
      {
        "name": "SecretString",
        "desc": "新的凭据内容为文本的场景使用该字段，不需要base64编码。SecretBinary 和 SecretString 只能一个不为空。"
      }
    ],
    "desc": "该接口用于更新指定凭据名称和版本号的内容，调用该接口会对新的凭据内容加密后覆盖旧的内容。仅允许更新Enabled 和 Disabled 状态的凭据。"
  },
  "ListSecrets": {
    "params": [
      {
        "name": "Offset",
        "desc": "查询列表的起始位置，以0开始，不设置默认为0。"
      },
      {
        "name": "Limit",
        "desc": "单次查询返回的最大数量，0或不设置则使用默认值 20。"
      },
      {
        "name": "OrderType",
        "desc": "根据创建时间的排序方式，0或者不设置则使用降序排序， 1 表示升序排序。"
      },
      {
        "name": "State",
        "desc": "根据凭据状态进行过滤，默认为0表示查询全部，1 表示查询Enabed 凭据列表，2表示查询Disabled 凭据列表， 3 表示查询PendingDelete 凭据列表。"
      },
      {
        "name": "SearchSecretName",
        "desc": "根据凭据名称进行过滤，为空表示不过滤。"
      }
    ],
    "desc": "该接口用于获取所有凭据的详细列表，可以指定过滤字段、排序方式等。"
  },
  "DescribeSecret": {
    "params": [
      {
        "name": "SecretName",
        "desc": "指定需要获取凭据详细信息的凭据名称。"
      }
    ],
    "desc": "获取凭据的详细属性信息。"
  },
  "GetServiceStatus": {
    "params": [],
    "desc": "该接口用户获取用户SecretsManager服务开通状态。"
  },
  "DeleteSecretVersion": {
    "params": [
      {
        "name": "SecretName",
        "desc": "指定凭据名称。"
      },
      {
        "name": "VersionId",
        "desc": "指定该名称下需要删除的凭据的版本号。"
      }
    ],
    "desc": "该接口用于直接删除指定凭据下的单个版本凭据，删除操作立即生效，对所有状态下的凭据版本都可以删除。"
  },
  "UpdateDescription": {
    "params": [
      {
        "name": "SecretName",
        "desc": "指定需要更新描述信息的凭据名。"
      },
      {
        "name": "Description",
        "desc": "新的描述信息，最大长度2048个字节。"
      }
    ],
    "desc": "该接口用于修改指定凭据的描述信息，仅能修改Enabled 和 Disabled 状态的凭据。"
  },
  "GetRegions": {
    "params": [],
    "desc": "获取控制台展示region列表"
  },
  "DisableSecret": {
    "params": [
      {
        "name": "SecretName",
        "desc": "指定停用的凭据名称。"
      }
    ],
    "desc": "停用指定的凭据，停用后状态为 Disabled，无法通过接口获取该凭据的明文。"
  },
  "GetSecretValue": {
    "params": [
      {
        "name": "SecretName",
        "desc": "指定凭据的名称。"
      },
      {
        "name": "VersionId",
        "desc": "指定对应凭据的版本号。"
      }
    ],
    "desc": "获取指定凭据名称和版本的凭据明文信息，只能获取启用状态的凭据明文。"
  }
}