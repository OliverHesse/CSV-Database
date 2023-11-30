import csv
import os
import time  #not nessecary only for speed test

import csv
import os
import time  #not nessecary only for speed test
from icecream import ic #not nessecary only for debuging

class node:

  def __init__(self, value, index):
    self.value = value
    self.row_index = [index]
    self.left = None
    self.right = None

  def insert_new_node(self, value, index):

    if value > self.value:
      #go right
      if self.right is not None:
        self.right.insert_new_node(value, index)
      else:
        self.right = node(value, index)
    elif value < self.value:
      #go left
      if self.left is not None:
        self.left.insert_new_node(value, index)
      else:
        self.left = node(value, index)
    else:
      #increase count in this node
      self.row_index.append(index)

  def Output(self):
    output = ""
    if self.left is not None:
      output += str(self.left.Output()) + ","
    output += str(self.value)
    if self.right is not None:
      output += "," + str(self.right.Output())
    return output

  def search(self, operator: str, value):

    #operator only supports ==, <, >, <=, >=, !=
    if operator == "==":

      if value == self.value:
        return self.row_index
      else:
        if value > self.value:
          #go right
          if self.right is not None:
            return self.right.search(operator, value)
          return None
        else:
          #go left
          if self.left is not None:
            return self.left.search(operator, value)
          return None
    elif operator == ">=":
      if self.value >= value:
        returnV = []
        #check both left and right
        if self.right is not None:
          returnV += self.right.search(operator, value)
        if self.left is not None:
          returnV += self.left.search(operator, value)
        return self.row_index + returnV
      else:
        #check only right
        if self.right is not None:
          return self.right.search(operator, value)
        return []
    elif operator == "<=":

      if self.value <= value:
        returnV = []
        #check both left and right
        if self.right is not None:
          returnV += self.right.search(operator, value)
        if self.left is not None:
          returnV += self.left.search(operator, value)

        return self.row_index + returnV
      else:
        #check only left
        if self.left is not None:
          return self.left.search(operator, value)
        return []
    elif operator == "<":
      if self.value < value:
        returnV = []
        #check both left and right
        if self.right is not None:
          returnV += self.right.search(operator, value)
        if self.left is not None:
          returnV += self.left.search(operator, value)

        return self.row_index + returnV
      else:
        #check only left
        if self.left is not None:
          return self.left.search(operator, value)
        return []
    elif operator == ">":
      if self.value > value:

        returnV = []
        #check both left and right
        if self.right is not None:
          returnV += self.right.search(operator, value)
        if self.left is not None:
          returnV += self.left.search(operator, value)
        return self.row_index + returnV
      else:
        #check only right
        if self.right is not None:
          return self.right.search(operator, value)
        return []
    elif operator == "!=":
      returnV = []
      if self.left is not None:
        returnV += self.left.search(operator, value)
      if self.value != value:
        returnV += self.row_index
      if self.right is not None:
        returnV += self.right.search(operator, value)
      return returnV

  def get_all(self):
    output = []
    if self.left is not None:
      output += self.left.get_all()
    output += [self.value]
    if self.right is not None:
      output += self.right.get_all()

  def max(self):
    if self.right is not None:
      return self.right.max()
    else:
      return self.value

  def min(self):
    if self.left is not None:
      return self.left.max()
    else:
      return self.value

  def max_branch_node_ref(self):

    if self.right is not None:

      return self.right.max_branch_node_ref()
    else:

      return self
  def min_branch_node_ref(self):

    if self.left is not None:
      return self.left.min_branch_node_ref()
    else:
      return self
  def delete_node(self, value, index):
    if value > self.value:
      #go right
      if self.right is not None:
        if value == self.right.value:
          if index in self.right.row_index:
            #delete this node
            if self.right.left is None and self.right.right is None:
              self.right = None
            else:
              if self.right.left is not None and self.right.right is not None:
                temp_ref = self.right
                self.right = self.right.left
                new_ref = self.right.max_branch_node_ref()
                new_ref.right = temp_ref.right
                temp_ref = None
              elif self.right.right is not None:
                temp_ref = self.right
                self.right = temp_ref.right
                temp_ref = None
              else:
                temp_ref = self.right
                self.right = self.right.left
                temp_ref = None
        else:
          self.right.delete_node(value, index)

    else:
      #go left
      if self.left is not None:
        if value == self.left.value:
          if index in self.left.row_index:
            #delete this node
            if self.left.left is None and self.left.right is None:
              self.left = None
            else:
              if self.left.left is not None and self.left.right is not None:
                temp_ref = self.left
                self.left = self.left.right
                new_ref = self.right.min_branch_node_ref()

                new_ref.left = temp_ref.left
                temp_ref = None
              elif self.left.right is not None:
                temp_ref = self.left
                self.left = temp_ref.right
                temp_ref = None
              else:
                temp_ref = self.left
                self.left = self.right.left
                temp_ref = None
        else:
          self.left.delete_node(value, index)


class BinaryTree:

  def __init__(self, values=None):
    if values is not None:
      self.rootNode = node(values[0][0], values[0][1])
      for i in range(1, len(values)):

        self.rootNode.insert_new_node(values[i][0], values[i][1])
    else:
      self.rootNode = None

  def __str__(self):
    output = self.rootNode.Output()
    return output

  def search(self, value, operator: str):
    #operator only supports ==, <, >, <=, >=, !=
    return self.rootNode.search(value, operator)

  def max(self):
    if self.rootNode is not None:
      return self.rootNode.max()

  def min(self):
    if self.rootNode is not None:
      return self.rootNode.min()

  def get_all(self):
    if self.rootNode is not None:
      return self.rootNode.get_all()

  def add_node(self, values):

    if self.rootNode is not None:

      self.rootNode.insert_new_node(values[0], values[1])
    else:
      self.rootNode = node(values[0], values[1])

  def delete_node(self, values):
    value = values[0]
    index = values[1]
    if values[0] == self.rootNode.value:
      if values[1] in self.rootNode.row_index:
        if self.rootNode.right is None and self.rootNode.left is None:
          self.rootNode = None
        else:
          if self.rootNode.left is not None and self.rootNode.right is not None:
            temp_ref = self.rootNode
            self.rootNode = self.rootNode.left
            new_ref = self.rootNode.max_branch_node_ref()
            new_ref.right = temp_ref.right
            temp_ref = None
          elif self.rootNode.right is not None:
            temp_ref = self.rootNode
            self.rootNode = temp_ref.right
            temp_ref = None
          else:
            temp_ref = self.rootNode
            self.rootNode = self.rootNode.left
            temp_ref = None
    elif value > self.rootNode.value:
      #go right
      if self.rootNode.right is not None:
        if value == self.rootNode.right.value:
          if index in self.rootNode.right.row_index:
            #delete this node
            if self.rootNode.right.left is None and self.rootNode.right.right is None:
              self.rootNode.right = None
            else:
              if self.rootNode.right.left is not None and self.rootNode.right.right is not None:
                temp_ref = self.rootNode.right
                self.rootNode.right = self.rootNode.right.left
                new_ref = self.rootNode.right.max_branch_node_ref()
                new_ref.right = temp_ref.right
                temp_ref = None
              elif self.rootNode.right.right is not None:
                temp_ref = self.rootNode.right
                self.rootNode.right = temp_ref.right
                temp_ref = None
              else:
                temp_ref = self.rootNode.right
                self.rootNode.right = self.rootNode.right.left
                temp_ref = None
        else:
          self.rootNode.right.delete_node(value, index)

    elif value < self.rootNode.value:
      #go left
      if self.rootNode.left is not None:
        if value == self.rootNode.left.value:
          if index in self.rootNode.left.row_index:
            #delete this node
            if self.rootNode.left.left is None and self.rootNode.left.right is None:
              self.rootNode.left = None
            else:
              if self.rootNode.left.left is not None and self.rootNode.left.right is not None:
                temp_ref = self.rootNode.left
                self.rootNode.left = self.rootNode.left.right

                new_ref = self.rootNode.left.min_branch_node_ref()

                new_ref.left = temp_ref.left
                temp_ref = None
              elif self.rootNode.left.right is not None:
                temp_ref = self.rootNode.left
                self.rootNode.left = temp_ref.right
                temp_ref = None
              else:
                temp_ref = self.rootNode.left
                self.rootNode.left = self.rootNode.right.left
                temp_ref = None
        else:
          self.rootNode.left.delete_node(value, index)


    else:
      self.rootNode.delete_node(values[0], values[1])


class Database:

  def __init__(self, db_folder):
    self.db_folder = os.getcwd() + "/" + db_folder
    self.tables = {}
    self.tableFileType = ".csv"
    for filename in os.listdir(path=self.db_folder):
      if filename.endswith(self.tableFileType):
        self.tables[filename.replace(".csv", "")] = Table(
          f"{self.db_folder}/{filename}", filename.strip(".csv"))
    print("DB SETUP")

  def MAX(self, table_name, column, where=None):
    return self.tables[table_name].MAX(column, where)

  def MIN(self, table_name, column, where=None):
    return self.tables[table_name].MIN(column, where)

  def TOTAL(self, table_name, column, where=None):
    return self.tables[table_name].TOTAL(column, where)

  def commit(self):
    for table_name in self.tables:
      self.tables[table_name].commit()

  def execute(self, statement):

    keyWords = [
      "SELECT", "INSERT", "UPDATE", "FROM", "WHERE", "INTO", "SET", "VALUES"
    ]
    keyWordsMinor = ["AND", "OR"]
    keyWordsPresence = {
      "SELECT": False,
      "INSERT": False,
      "UPDATE": False,
      "FROM": False,
      "WHERE": False,
      "AND": False,
      "OR": False
    }
    if type(statement) != str:
      raise Exception("Error: cannot parse non string statement")
    else:

      nonWhitespace = statement.replace(" ", "")

      if nonWhitespace.find("SELECT") != 0 and nonWhitespace.find(
          "INSERT") != 0 and nonWhitespace.find("UPDATE") != 0:
        raise Exception("Error: must start with SELECT, INSERT OR UPDATE")
      keyWordLocal = []
      keyWordLocal2 =[]
      for i in keyWords:
        locationIndex = nonWhitespace.find(i)
        if locationIndex != -1:

          keyWordsPresence[i] = True
          keyWordLocal.append([nonWhitespace.find(i), i])
      for i in keyWords:
        locationIndex = statement.find(i)
        if locationIndex != -1:

          keyWordsPresence[i] = True
          keyWordLocal2.append([statement.find(i), i])
      #for actual project use own sorting algo
      keyWordLocal.sort()
      keyWordLocal2.sort()
      statementArray = {}
      statementArray2 = {}
      for index in range(0, len(keyWordLocal) - 1):
        cmd = nonWhitespace[keyWordLocal[index][0]:keyWordLocal[index + 1][0]][
          0:len(keyWordLocal[index][1])]

        cmdInput = nonWhitespace[keyWordLocal[index][0]:keyWordLocal[index + 1]
                                 [0]][len(keyWordLocal[index][1]):]
        statementArray[cmd] = cmdInput
      for index in range(0, len(keyWordLocal2)-1):
        cmd2 = statement[keyWordLocal2[index][0]:keyWordLocal2[index + 1][0]][
        0:len(keyWordLocal2[index][1])]
        cmd2Input = statement[keyWordLocal2[index][0]:keyWordLocal2[index + 1]
         [0]][len(keyWordLocal2[index][1]):]
        statementArray2[cmd2] = cmd2Input

      #seperates the cmd and the arguments
      cmd = nonWhitespace[keyWordLocal[-1][0]:][0:len(keyWordLocal[-1][1])]
      cmdInput = nonWhitespace[keyWordLocal[-1][0]:][len(keyWordLocal[-1][1]):]
      statementArray[cmd] = cmdInput
      cmd2 = statement[keyWordLocal2[-1][0]:][0:len(keyWordLocal2[-1][1])]
      cmd2Input = statement[keyWordLocal2[-1][0]:][len(keyWordLocal2[-1][1]):]
      statementArray2[cmd2] = cmd2Input

      if "FROM" not in statementArray and "INTO" not in statementArray and "UPDATE" not in statementArray:
        raise Exception("Error: no table provided")
      if keyWordsPresence["UPDATE"] == True:

        return self.tables[statementArray["UPDATE"]].execute(
          statementArray, keyWordsPresence,statementArray2)
      if keyWordsPresence["SELECT"] == True:
        return self.tables[statementArray["FROM"]].execute(
          statementArray, keyWordsPresence,statementArray2)
      if keyWordsPresence["INSERT"] == True:

        return self.tables[statementArray["INTO"]].execute(
          statementArray, keyWordsPresence,statementArray2)

  def setup_from_csv(self, file_path):
    file = open(file_path + ".csv", "r")
    reader = csv.reader(file)

    for row in reader:
      table_name = ""
      columnCount = 0
      columns = []
      for column in row:
        if columnCount == 0:
          table_name = column

        else:
          columns.append(column.split(":"))
        columnCount += 1
      #create new table with data
      if table_name not in self.tables:
        self.create(table_name, columns)
    file.close()

  def create(self, table_name, columns):
    #columns should be in format [[c1 , type],[c2,type]]
    file = open(self.db_folder + "/" + table_name + ".csv", "w")
    row_text = []
    for column in columns:
      if len(column) != 2:
        raise Exception("Error: column not recognised")
      match column[1]:
        case "int":
          pass
        case "str":
          pass
        case "float":
          pass
        case "bool":
          pass
        case _:
          raise Exception("Error: Invalid Data Type")
      row_text.append(str(column[0]) + ":" + str(column[1]))
    writer = csv.writer(file)
    writer.writerow(row_text)
    file.close()
    self.tables[table_name] = Table(self.db_folder + "/" + table_name + ".csv",
                                    table_name)


class Table:
  keyword = ["Primary", "Integer"]

  def __init__(self, filePath, name):
    self.tableName = name

    self.tableFilePath = filePath
    table_file = open(filePath, "r")
    csv_reader = csv.reader(table_file, delimiter=',')
    count = 0
    self.ColumnMetaData = {}
    self.table = []
    tempMap = {}
    for row in csv_reader:
      if count == 0:
        for header_i in range(0, len(row)):
          column_meta = row[header_i].split(":")
          if len(column_meta) != 2:
            raise Exception(
              "cannot parse: column header must include Name:Type")
          tempMap[header_i] = {
            "columnName": column_meta[0],
            "columnType": column_meta[1]
          }
          self.ColumnMetaData[column_meta[0]] = {
            "column_id": header_i,
            "type": column_meta[1],
            "searchTree": BinaryTree()
          }

      else:
        self.table.append([])
        for header_i in range(0, len(row)):
          #check if it is corect data type and insert into table

          try:
            value = None
            if tempMap[header_i]["columnType"] == "int":
              self.table[count - 1].append(int(row[header_i]))
              value = int(row[header_i])
            if tempMap[header_i]["columnType"] == "str":
              self.table[count - 1].append(str(row[header_i]))
              value = str(row[header_i])
            if tempMap[header_i]["columnType"] == "float":
              self.table[count - 1].append(float(row[header_i]))
              value = float(row[header_i])
            if tempMap[header_i]["columnType"] == "bool":
              self.table[count - 1].append(bool("True" == row[header_i]))
              value = bool("True" == row[header_i])

            self.ColumnMetaData[tempMap[header_i]
                                ["columnName"]]["searchTree"].add_node(
                                  [value, count - 1])
          except:
            raise Exception(
              "cannot read table: field type does not match column type")
      count += 1

  def where(self, statementArray, keyWordsPresence,statementArray2):
    keyWords = ["SELECT", "INSERT", "UPDATE", "FROM", "WHERE", "INTO", "SET"]
    keyWordsMinor = ["AND", "OR"]
    if statementArray["WHERE"].find("AND") != -1:
      keyWordsPresence["AND"] = True
    if statementArray["WHERE"].find("OR") != -1:
      keyWordsPresence["OR"] = True
    statementArray2["WHERE"].strip()
    if keyWordsPresence["AND"] == True or keyWordsPresence["OR"] == True:
      laststatementIndex = 0
      lastFoundIndex = 0
      allIndex = []
      IndexMap = {}
      allStIndex = []
      IndexStMap = {}
      for key in keyWordsMinor:
        laststatementIndex = 0
        lastFoundIndex = 0
        for i in range(0, statementArray["WHERE"].count(key)):
          lastFoundIndex = statementArray["WHERE"].find(
            key, lastFoundIndex + 1)
          laststatementIndex = statementArray2["WHERE"].find(
            key, lastFoundIndex + 1)
          allIndex.append(lastFoundIndex)
          allStIndex.append(laststatementIndex)
          IndexStMap[laststatementIndex] = key
          IndexMap[lastFoundIndex] = key
      allIndex.sort()
      allStIndex.sort()
      statementArray2 = statementArray2["WHERE"].replace("AND","<?>").replace("OR","<?>").split("<?>")
      statementArray["WHERE"] = statementArray["WHERE"].replace(
        "AND", " ").replace("OR", " ").split()

      index_result = []

      for arguement_i in range(0, len(statementArray["WHERE"])):
        arguement = statementArray["WHERE"][arguement_i]
        arg = statementArray2["WHERE"][arguement_i].strip()
        #only supports ==, <=, >=, <, >, !=
        operand = ""
        if arguement.find("==") != -1:

          operand = "=="
        elif arguement.find("!=") != -1:
          operand = "!="
        elif arguement.find("<=") != -1:
          operand = "<="
        elif arguement.find(">=") != -1:
          operand = ">="
        elif arguement.find("<") != -1:
          operand = "<"
        elif arguement.find(">") != -1:
          operand = ">"
        indexLocal = arg.find(operand)

        column = arg[0:indexLocal].strip()
        value = None

        try:

          if self.ColumnMetaData[column]["type"] == "int":
            value = int(arg[indexLocal + len(operand):])

          if self.ColumnMetaData[column]["type"] == "str":
            value = str(arg[indexLocal + len(operand):]).strip()
          if self.ColumnMetaData[column]["type"] == "float":
            value = float(arg[indexLocal + len(operand):])
          if self.ColumnMetaData[column]["type"] == "bool":
            value = bool("True" == arg[indexLocal + len(operand):].strip())

        except:
          raise Exception(
            "cannot read table: field type does not match column type")

        result = self.ColumnMetaData[column]["searchTree"].search(
          operand, value)  # do binary tree search here

        index_result.append(result)
      if len(index_result) == 0:
        return None
      final_array = index_result[0]

      for i in range(0, len(allIndex)):

        if IndexMap[allIndex[i]] == "AND":
          temp = []

          for item in final_array:
            for item2 in index_result[i + 1]:
              if item2 == item:
                temp.append(item2)
          final_array = temp
        elif IndexMap[allIndex[i]] == "OR":

          for item in index_result[i + 1]:
            if item not in final_array:
              final_array.append(item)
        #do a table search with final array and return results


      return final_array
    else:
      #easey parse #no and or or
      arguement = statementArray["WHERE"]

      arg = statementArray2["WHERE"]
      #only supports ==, <=, >=, <, >, !=
      operand = ""
      if arg.find("==") != -1:

        operand = "=="
      elif arg.find("!=") != -1:
        operand = "!="
      elif arg.find("<=") != -1:
        operand = "<="
      elif arg.find(">=") != -1:
        operand = ">="
      elif arg.find("<") != -1:
        operand = "<"
      elif arg.find(">") != -1:
        operand = ">"
      else:
        raise Exception("error: by WHERE")
      indexLocal = arg.find(operand)
      column = arg[0:indexLocal].strip()
      value = None
      try:
        print(self.ColumnMetaData[column]["type"])
        if self.ColumnMetaData[column]["type"] == "int":
          value = int(arg[indexLocal + len(operand):])

        if self.ColumnMetaData[column]["type"] == "str":
          value = str(arg[indexLocal + len(operand):]).strip()
        if self.ColumnMetaData[column]["type"] == "float":
          value = float(arg[indexLocal + len(operand):])
        if self.ColumnMetaData[column]["type"] == "bool":
          value = bool("True" == arg[indexLocal + len(operand):].strip())

      except:
        raise Exception(
          "cannot read table: field type does not match column type")
      result = self.ColumnMetaData[column]["searchTree"].search(
        operand, value)  # do binary tree search here

      return result

  def commit(self):
    table_file = open(self.tableFilePath, mode='w')

    table_writer = csv.writer(table_file, delimiter=',')
    appendList = []
    for key in self.ColumnMetaData:
      appendList.append(f"{key}:{self.ColumnMetaData[key]['type']}")
    table_writer.writerow(appendList)
    for row in self.table:
      table_writer.writerow(row)
    table_file.close()

  def insert(self, statementArray, keyWordsPresence,statement):
    values = statement["VALUES"].strip().split(",")

    if len(values) != len(self.ColumnMetaData):
      raise Exception(
        "Error: number arguments provided do not match number of arguments needed "
      )
    for key in self.ColumnMetaData:
      value = None
      try:
        if self.ColumnMetaData[key]["type"] == "int":
          value = int(values[self.ColumnMetaData[key]["column_id"]].strip())
        if self.ColumnMetaData[key]["type"] == "str":
          value = str(values[self.ColumnMetaData[key]["column_id"]]).strip()
        if self.ColumnMetaData[key]["type"] == "float":
          value = float(values[self.ColumnMetaData[key]["column_id"]])
        if self.ColumnMetaData[key]["type"] == "bool":

          value = bool("True" == values[self.ColumnMetaData[key]["column_id"]].strip())
      except:
        raise Exception(
          "Error: argument data type does not match column data type")

      self.ColumnMetaData[key]["searchTree"].add_node([value, len(self.table)])
    self.table.append(values)
    return {"status": "complete"}

  def select(self, statementArray, keyWordsPresence,statement):
    if len(self.table) == 0:
      return []
    keyWords = ["SELECT", "INSERT", "UPDATE", "FROM", "WHERE", "INTO", "SET"]
    keyWordsMinor = ["AND", "OR"]
    columnsToSelect = []
    if statementArray["SELECT"] != "*":
      columnsToSelect = statementArray["SELECT"].split(",")
    else:
      for key in self.ColumnMetaData:
        columnsToSelect.append(key)

    #do all the table selecion stuff up here
    if keyWordsPresence["WHERE"] == True:

      rows = self.where(statementArray, keyWordsPresence,statement)
      indexes = []
      if rows is None:
        return []
      for column in columnsToSelect:
        indexes.append(self.ColumnMetaData[column]["column_id"])
      output = []
      for row_i in rows:
        output.append(list(self.table[row_i][i] for i in indexes))
      return output
    else:
      indexes = []
      for column in columnsToSelect:
        indexes.append(self.ColumnMetaData[column]["column_id"])
      output = []
      for row_i in range(0, len(self.table)):
        output.append(list(self.table[row_i][i] for i in indexes))
      return output

  def execute(self, statementArray, keyWordsPresence,statement):

    keyWords = [
      "SELECT", "INSERT", "UPDATE", "FROM", "WHERE", "INTO", "SET", "VALUES","DELETE"
    ]
    keyWordsMinor = ["AND", "OR"]
    if keyWordsPresence["SELECT"] == True:
      return self.select(statementArray, keyWordsPresence,statement)
    if keyWordsPresence["INSERT"] == True:
      if keyWordsPresence["VALUES"] != True:
        raise Exception("Error: cannot inserrt into table no values provided")
      return self.insert(statementArray, keyWordsPresence,statement)
    if keyWordsPresence["UPDATE"] == True:
      if keyWordsPresence["SET"] != True:
        raise Exception("Error: cannot update no set values provided")
      return self.update(statementArray, keyWordsPresence,statement)
    if keyWordsPresence["DELETE"] == True:
      if keyWordsPresence["WHERE"] != True:
        raise Exception("Error: cannot delete no where clause provided")
      return self.delete(statementArray, keyWordsPresence,statement)
  def delete(self, statementArray, keyWordsPresence,statement):
    pass
  def update(self, statementArray, keyWordsPresence,statement):
    if len(self.table) == 0:
      return None
    keyWords = ["UPDATE", "WHERE", "SET"]
    keyWordsMinor = ["AND", "OR"]

    SegemntStatement = statement["SET"].strip().split(",")
    #find column to update
    updateValueMap = {}
    for updateStatement in SegemntStatement:
      operand = updateStatement.find("=")
      if operand == -1:
        raise Exception("Error:missing = in statement")
      columnName = updateStatement[:operand].strip()
      columnValue = updateStatement[operand + 1:].strip()
      if columnName not in self.ColumnMetaData:
        raise Exception("Error: column cannot be found")
      try:
        if self.ColumnMetaData[columnName]["type"] == "int":
          int(columnValue)
        if self.ColumnMetaData[columnName]["type"] == "str":
          str(columnValue)
        if self.ColumnMetaData[columnName]["type"] == "float":
          float(columnValue)
        if self.ColumnMetaData[columnName]["type"] == "bool":
          bool("True" == columnValue)
      except:
        raise Exception("Error: value type does not match column type")
      updateValueMap[columnName] = {
        "column_id": self.ColumnMetaData[columnName]["column_id"],
        "value": columnValue
      }

    #do where statement
    rows = self.where(statementArray, keyWordsPresence,statement)

    for row in rows:
      for key in updateValueMap:

        self.table[row][updateValueMap[key]["column_id"]] = updateValueMap[key]["value"]
    return {"status": "complete"}

  def MAX(self, column, where=None):
    if len(self.table) == 0:
      return -1
    if column in self.ColumnMetaData:
      if self.ColumnMetaData[column]["type"] == "float" or self.ColumnMetaData[
          column]["type"] == "int":
        if where is not None:
          max_value_row_id = where({"WHERE": where}, {
            "AND": False,
            "OR": False
          })[-1]
          column_id = self.ColumnMetaData[column]["column_id"]
          if self.ColumnMetaData[column]["type"] == "float":
            return float(self.table[max_value_row_id][column_id])
          else:
            return int(self.table[max_value_row_id][column_id])
        else:
          if self.ColumnMetaData[column]["type"] == "float":
            return float(self.ColumnMetaData[column]["searchTree"].max())
          else:
            return int(self.ColumnMetaData[column]["searchTree"].max())
      raise Exception(
        f"Error: Column data type must be float or int not {self.ColumnMetaData[column]['type']}"
      )
    raise Exception("Error: Column no recognised")

  def MIN(self, column, where=None):
    if len(self.table) == 0:
      return -1
    if column in self.ColumnMetaData:
      if self.ColumnMetaData[column]["type"] == "float" or self.ColumnMetaData[
          column]["type"] == "int":
        if where is not None:
          max_value_row_id = where({"WHERE": where}, {
            "AND": False,
            "OR": False
          })[0]
          column_id = self.ColumnMetaData[column]["column_id"]
          if self.ColumnMetaData[column]["type"] == "float":
            return float(self.table[max_value_row_id][column_id])
          else:
            return int(self.table[max_value_row_id][column_id])
        else:
          if self.ColumnMetaData[column]["type"] == "float":
            return float(self.ColumnMetaData[column]["searchTree"].min())
          else:
            return int(self.ColumnMetaData[column]["searchTree"].min())
      raise Exception(
        f"Error: Column data type must be float or int not {self.ColumnMetaData[column]['type']}"
      )
    raise Exception("Error: Column no recognised")

  def TOTAL(self, column, where):
    if len(self.table == 0):
      return 0
    if column in self.ColumnMetaData:
      where = where.replace(" ","")
      if self.ColumnMetaData[column]["type"] == "float" or self.ColumnMetaData[
          column]["type"] == "int":

        if where is not None:
          rows = self.where({"WHERE": where}, {"AND": False, "OR": False})
          column_id = self.ColumnMetaData[column]["column_id"]

          if self.ColumnMetaData[column]["type"] == "float":
            total = 0

            for row_i in range(0,len(rows)):
              total += float(self.table[rows[row_i]][self.ColumnMetaData[column]["column_id"]])
            return total
          else:
            total = 0

            for row_i in range(0,len(rows)):

              total += int(self.table[rows[row_i]][self.ColumnMetaData[column]["column_id"]])
            return total
        else:

          values = self.ColumnMetaData[column]["searchTree"].get_all()
          if self.ColumnMetaData[column]["type"] == "float":
            total = 0
            for value in values:
              total += float(value)
            return total
          else:
            total = 0
            for value in values:
              total += int(value)
            return total
      raise Exception(
        f"Error: Column data type must be float or int not {self.ColumnMetaData[column]['type']}"
      )
    raise Exception("Error: Column no recognised")


def run_test():
  runningTimeTotal = 0
  itr = 10000
  for i in range(0, itr):
    start = time.time()

    value = db.execute("SELECT * FROM table1 WHERE id >= 1 OR name == Oliver")
    runningTimeTotal += time.time() - start

  print("total time taken: " + str(runningTimeTotal))
  print("average time taken: " + str(runningTimeTotal / itr))


if __name__ == "__main__":
  db = Database("database")
  print("started")
  run_test()
