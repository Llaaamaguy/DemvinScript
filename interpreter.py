"""
   Copyright 2022 Devin Kennedy

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from wit import Wit
import os
from Nodes import *

token = os.environ["WIT_TOKEN"]
client = Wit(token)


def parse_value(value):
    try:
        int(value)
    except ValueError:
        return StrNode(value)
    if "." in [x for x in value]:
        return FloatNode(value)
    else:
        return IntNode(value)


def main():
    with open("code.txt", "r") as f:
        lines = f.readlines()

    varStore = {}

    for line in lines:
        if line.strip():
            result = client.message(line)
            linetype = result["intents"][0]["name"]
            # print(f"{lines.index(line)}: {linetype}")
            if linetype == "var_def":
                try:
                    varName = result["entities"]["var_name:var_name"][0]["body"]
                    varVal = result["entities"]["var_value:var_value"][0]["body"]
                    varStore[varName] = VarNode(varName, parse_value(varVal))
                except KeyError:
                    try:
                        varName = result["entities"]["var_name:var_name"][0]["body"]
                        eval_left = result["entities"]["eval_left:eval_left"][0]["body"]
                        eval_right = result["entities"]["eval_right:eval_right"][0]["body"]
                        eval_op = result["entities"]["eval_operator:eval_operator"][0]["body"]
                        if eval_left in list(varStore.keys()):
                            eval_left = str(varStore[eval_left].varValue)
                        if eval_right in list(varStore.keys()):
                            eval_right = str(varStore[eval_right].varValue)
                        if eval_op == "+":
                            varStore[varName] = VarNode(varName, PlusNode(parse_value(eval_left), parse_value(eval_right)).eval())
                        elif eval_op == "*":
                            varStore[varName] = VarNode(varName, TimesNode(parse_value(eval_left), parse_value(eval_right)).eval())
                    except KeyError:
                        print(f"WARNING ON {line}: All entities not found\nIgnoring variable definition")
                    pass
            elif linetype == "output":
                try:
                    toPrint = result["entities"]["out_val:out_val"][0]["body"]
                    if toPrint in list(varStore.keys()):
                        toPrint = str(varStore[toPrint])
                    print(f"SYS-OUT: {toPrint}")
                except KeyError:
                    print(f"WARNING ON {line}: All entities not found\nIgnoring output statement")
        else:
            # print(f"{lines.index(line)}: Empty line")
            pass

    # print(varStore)


if __name__ == "__main__":
    main()
