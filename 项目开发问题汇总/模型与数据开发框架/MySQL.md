明白，下面我将提供一个总框架，先概述整个流程，然后再细化每一步的具体操作，以确保项目顺利推进。

---

## 总体框架：MySQL 数据库构建与数据整合流程

1. **数据库初始化与表格创建**
   - 目标：在 `BP_Prediction_Database` 中创建项目所需的 5 张数据表。
   - 步骤概览：创建基础表结构、配置主键和外键关系、定义字段类型。

2. **数据存储逻辑设计**
   - 目标：确保数据插入、更新和查询的逻辑高效且一致。
   - 步骤概览：设计数据插入顺序、关联关系的维护方法、数据清理策略。

3. **测试与验证**
   - 目标：通过插入测试数据，验证数据表的关系和查询的准确性。
   - 步骤概览：插入测试数据、验证查询结果、测试关联关系。

4. **准备数据操作脚本**
   - 目标：编写脚本实现数据的自动化插入、更新和清理，以减少人工操作。
   - 步骤概览：编写SQL脚本或Python连接MySQL脚本，实现批量数据操作。

---

接下来，我们按以上步骤进行细化。

---

### 1. 数据库初始化与表格创建

**步骤 1.1**: 打开 MySQL Workbench，连接到 `BP_Prediction_Database`。

**步骤 1.2**: 逐个创建所需的表格，字段和数据类型建议如下：
- **PatientInfo**：包含患者基础信息字段。
- **HealthMonitoring**：存储患者的监测数据（例如血压数据）。
- **TrainingData**：包含用于模型训练的特征数据。
- **PredictionResults**：记录模型的预测输出及相关信息。
- **IDMapping**：关联`UserPatientID`和`UUIDPatientID`，便于快速映射和查询。

**步骤 1.3**: 为每个表设置主键，例如 `PatientInfo` 表的 `UUIDPatientID`，然后为其他表（如 `HealthMonitoring`）配置外键，关联 `UUIDPatientID`，确保数据关系的完整性。

---

### 2. 数据存储逻辑设计

**步骤 2.1**: **数据插入逻辑**
   - **IDMapping**：每当创建新患者时，先生成 `UserPatientID` 和 `UUIDPatientID`，插入 `IDMapping` 表。
   - **PatientInfo**：在 `IDMapping` 成功插入后，插入 `PatientInfo`，确保该患者的基本信息存储完成。
   - **关联数据表**（如 `HealthMonitoring`、`TrainingData` 和 `PredictionResults`）：根据 `UUIDPatientID` 的外键关联到患者的其他数据表。

**步骤 2.2**: **数据更新和查询逻辑**
   - 设计标准的 SQL 查询语句，便于快速查询某个患者的所有健康监测数据、训练数据和预测结果。
   - 确保数据更新操作不影响关联关系（例如更新健康数据时不影响患者的基本信息）。

**步骤 2.3**: **数据清理和同步策略**
   - 根据项目需要，定义数据清理频率，例如定期归档旧数据，减少数据库存储压力。
   - 定义数据同步流程，确保模型生成的新预测结果能实时更新至数据库中。

---

### 3. 测试与验证

**步骤 3.1**: 插入样例数据
   - 插入一些样本患者信息、健康监测数据等，确保数据格式和插入逻辑的正确性。

**步骤 3.2**: 验证数据查询
   - 执行查询语句，确认跨表关联是否正确，例如，能否基于 `UUIDPatientID` 查询到患者的所有健康数据和预测结果。

**步骤 3.3**: 验证数据更新操作
   - 测试更新 `HealthMonitoring` 数据，确保更新不影响关联的患者信息数据。

---

### 4. 准备数据操作脚本

**步骤 4.1**: 编写SQL脚本
   - 编写标准的SQL插入和更新脚本，用于批量数据操作。
   - 编写SQL清理脚本，以实现数据的归档和自动清理。

**步骤 4.2**: 编写Python脚本（可选）
   - 若项目需要动态操作数据库，可以使用Python和MySQL Connector库，编写脚本实现数据的自动化处理，包括批量插入和查询。

---

按此框架逐步执行，我们可以确保数据表、数据存储逻辑、数据测试、以及数据操作脚本的完整性。每一步完成后，也可以随时进行验证，确保下一步在稳定的基础上推进。


如果你遇到错误并且整个 SQL 代码混乱，可以按照以下步骤彻底清理并重新设置表结构，确保每个表创建顺利，不会遇到外键约束的问题。以下是一个完整的 SQL 脚本，用于清理现有表并重新创建它们。

### 步骤 1: 删除所有相关表和外键约束

首先，清理所有表格，确保没有外键约束的问题。这会删除所有表，并且没有数据丢失的风险（如果数据已经备份或不需要）。

```sql
-- 删除所有相关表
DROP TABLE IF EXISTS HealthMonitoring;
DROP TABLE IF EXISTS TrainingData;
DROP TABLE IF EXISTS PredictionResults;
DROP TABLE IF EXISTS IDMapping;
DROP TABLE IF EXISTS PatientInfo;
```

### 步骤 2: 重新创建所有表

删除表之后，重新创建所有表并恢复外键约束。以下是完整的 SQL 代码来创建数据库所需的表格：

```sql
-- 重新创建 PatientInfo 表
CREATE TABLE PatientInfo (
    UUIDPatientID VARCHAR(36) PRIMARY KEY,
    UserPatientID VARCHAR(12) UNIQUE NOT NULL,
    Name VARCHAR(50),
    Gender VARCHAR(6),
    Age INT,
    Status VARCHAR(10),
    AuthLevel VARCHAR(10),
    CreatedAt DATETIME,
    UpdatedAt DATETIME
);

-- 重新创建 HealthMonitoring 表，并确保外键约束
CREATE TABLE HealthMonitoring (
    UUIDPatientID VARCHAR(36),
    SBP INT,
    DBP INT,
    MAP INT,
    BPV INT,
    HR INT,
    PWV INT,
    CentralBP INT,
    BMI FLOAT,
    BloodGlucose FLOAT,
    CholesterolLevel FLOAT,
    CreatedAt DATETIME,
    PRIMARY KEY (UUIDPatientID, CreatedAt),
    FOREIGN KEY (UUIDPatientID) REFERENCES PatientInfo(UUIDPatientID)
);

-- 重新创建 TrainingData 表
CREATE TABLE TrainingData (
    UUIDPatientID VARCHAR(36),
    TrainingDataID INT PRIMARY KEY,
    Data JSON,
    FOREIGN KEY (UUIDPatientID) REFERENCES PatientInfo(UUIDPatientID)
);

-- 重新创建 PredictionResults 表
CREATE TABLE PredictionResults (
    UUIDPatientID VARCHAR(36),
    PredictedRiskLevel VARCHAR(20),
    Suggestions TEXT,
    PredictionDate DATETIME,
    FOREIGN KEY (UUIDPatientID) REFERENCES PatientInfo(UUIDPatientID)
);

-- 重新创建 IDMapping 表
CREATE TABLE IDMapping (
    UserPatientID VARCHAR(12),
    UUIDPatientID VARCHAR(36) PRIMARY KEY,
    FOREIGN KEY (UserPatientID) REFERENCES PatientInfo(UserPatientID)
);
```

### 解释：

1. **`DROP TABLE IF EXISTS`**: 在创建新表之前，删除已经存在的表，避免表格冲突。
2. **`PatientInfo` 表**：存储患者的基本信息，包括 UUID 和 UserPatientID，`UUIDPatientID` 是主键。
3. **`HealthMonitoring` 表**：存储健康监测数据，外键 `UUIDPatientID` 引用 `PatientInfo` 表的 `UUIDPatientID`。
4. **`TrainingData` 表**：存储训练数据，外键 `UUIDPatientID` 引用 `PatientInfo` 表的 `UUIDPatientID`。
5. **`PredictionResults` 表**：存储预测结果，外键 `UUIDPatientID` 引用 `PatientInfo` 表的 `UUIDPatientID`。
6. **`IDMapping` 表**：存储用户患者 ID 与 UUID 的映射，`UUIDPatientID` 是主键，`UserPatientID` 与 `PatientInfo` 表关联。

### 注意：

- **外键约束**：每个表格中的 `UUIDPatientID` 都是外键，指向 `PatientInfo` 表的 `UUIDPatientID`。因此，`PatientInfo` 表必须首先创建。
- **`JSON` 数据类型**：在 `TrainingData` 表中，`Data` 列使用了 `JSON` 数据类型。如果您不想使用 JSON 类型，可以根据需要修改此列。

### 总结：
以上步骤和代码清理了现有的表，并确保所有表格和外键关系都能顺利建立。如果执行时仍然出现问题，提供详细的错误信息，我可以帮助您进一步排查。


是的，您可以直接在 SQL 界面（如 MySQL Workbench）中运行 `LOAD DATA INFILE` 语句来导入 CSV 数据。以下是您可以执行的步骤：

### 执行步骤：
1. **打开 MySQL Workbench**：启动 MySQL Workbench 并连接到您的 MySQL 数据库。
2. **选择数据库**：确保您已经选择了正确的数据库，例如：
   ```sql
   USE BP_Prediction_Database;
   ```
   这样可以确保您将数据导入到正确的数据库中。

3. **运行 `LOAD DATA INFILE` 语句**：
   在 SQL 编辑器中输入您的 `LOAD DATA INFILE` 语句，例如：
   ```sql
   LOAD DATA INFILE 'D:/BP_Prediction_Project_MultiTable/data/patient_info.csv'
   INTO TABLE patient_info
   FIELDS TERMINATED BY ','
   ENCLOSED BY '"'
   LINES TERMINATED BY '\r\n'
   IGNORE 1 LINES;
   ```
   然后点击 **Execute** 按钮（闪电图标）运行语句。

4. **确认数据导入**：您可以运行以下查询来检查数据是否成功导入：
   ```sql
   SELECT * FROM patient_info LIMIT 10;
   ```

### 需要注意的事项：

1. **路径问题**：
   - 使用 `LOAD DATA INFILE` 时，路径通常应该使用正斜杠（`/`）而不是反斜杠（`\`）。
   - 您还需要确保 MySQL 具有访问该文件的权限。对于某些 MySQL 配置，您可能需要将文件放在 MySQL 数据目录中，或者启用 `LOCAL` 选项来从客户端加载数据。

2. **`LOAD DATA LOCAL INFILE`**：
   如果遇到权限错误，可以尝试在语句中使用 `LOCAL` 关键字，像这样：
   ```sql
   LOAD DATA LOCAL INFILE 'D:/BP_Prediction_Project_MultiTable/data/patient_info.csv'
   INTO TABLE patient_info
   FIELDS TERMINATED BY ','
   ENCLOSED BY '"'
   LINES TERMINATED BY '\r\n'
   IGNORE 1 LINES;
   ```
   这会让 MySQL 从客户端读取文件，而不是从服务器读取。

3. **权限问题**：
   - 如果您遇到 `ERROR 1045 (28000): Access denied for user` 等权限问题，可能是因为 MySQL 的配置禁止了 `LOCAL` 文件加载功能。您可以通过管理员权限调整 MySQL 配置或将文件放在 MySQL 服务器的数据目录下。

4. **如果您使用的是 Windows 系统**：
   - 路径分隔符必须是正斜杠 `/`，例如：`'D:/BP_Prediction_Project_MultiTable/data/patient_info.csv'`，而不是反斜杠。

只要确保文件路径正确、CSV 文件格式匹配、并且没有权限问题，就可以顺利导入数据。