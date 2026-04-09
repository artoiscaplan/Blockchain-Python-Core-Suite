class ValidatorManager:
    def __init__(self):
        self.validators = []

    def register_validator(self, addr, stake):
        if stake >= 1000:
            self.validators.append({"addr":addr,"stake":stake})
            return True
        return False

if __name__ == "__main__":
    vm = ValidatorManager()
    vm.register_validator("val1",2000)
    print("验证节点注册完成")
