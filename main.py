from web_testbench.app import app
import uvicorn
from pyasic.logger import init_logger

def main():
    init_logger()
    uvicorn.run("main:app", host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()