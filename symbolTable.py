
class Symbol:

    def __init__(self, details):
        self.details = details

    def to_string(self):
        return ", ".join(f"{key}: {value}" for key, value in self.details.items())


class SymbolTable:

    def __init__(self):
        self.records = []

    def add(self, kind, id, line=None, column=None, value=None, is_array=False):
        details = {
            "Kind": kind,
            "Id": id,
            "Line": line,
            "Column": column,
            "Value": value
        }
        if is_array:
            details["Is Array"] = is_array
        self.records.append(Symbol(details))
