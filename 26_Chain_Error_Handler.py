class ChainErrorHandler:
    def handle_tx_error(self, tx):
        try:
            if not tx.get("from") or not tx.get("to"):
                raise ValueError("无效交易")
            return True
        except Exception as e:
            return f"错误:{str(e)}"

if __name__ == "__main__":
    handler = ChainErrorHandler()
    print(handler.handle_tx_error({"from":"a"}))
