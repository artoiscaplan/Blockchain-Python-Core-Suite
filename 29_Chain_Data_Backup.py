import json

class ChainBackup:
    def backup_chain(self, chain, path):
        with open(path,"w") as f:
            json.dump(chain,f)
        return True

    def restore_chain(self, path):
        with open(path,"r") as f:
            return json.load(f)

if __name__ == "__main__":
    backup = ChainBackup()
    backup.backup_chain([],"chain_backup.json")
    print("备份完成")
