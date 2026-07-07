"""
步骤：
# 0. 导包
# 1. 创建日志器对象
# 2. 设置日志打印级别
    # logging.DEBUG 调试级别
    # logging.INFO 信息级别
    # logging.WARNING 警告级别
    # logging.ERROR 错误级别
    # logging.CRITICAL 严重错误级别
# 3. 创建处理器对象
    # 创建 输出到控制台 处理器对象
    # 创建 输出到日志文件 处理器对象
# 4. 创建日志信息格式
# 5. 将日志信息格式设置给处理器
    # 设置给 控制台处理器
    # 设置给 日志文件处理器
# 6. 给日志器添加处理器
    # 给日志对象 添加 控制台处理器
    # 给日志对象 添加 日志文件处理器
# 7. 打印日志
"""
import logging.handlers
import logging
import time

from config import BASE_DIR


def init_log_config(filename,when='midnight',interval=1,backupCount=3):
    # 1. 创建日志器对象
    logger = logging.getLogger()

    # 2. 设置日志打印级别
    logger.setLevel(logging.INFO)
    # logging.DEBUG 调试级别
    # logging.INFO 信息级别
    # logging.WARNING 警告级别
    # logging.ERROR 错误级别
    # logging.CRITICAL 严重错误级别

    # 3.1 创建 输出到控制台 处理器对象
    st = logging.StreamHandler()
    # 3.2 创建 输出到日志文件 处理器对象
    fh = logging.handlers.TimedRotatingFileHandler(filename, when=when, interval=interval,
                                                   backupCount=backupCount, encoding='utf-8')
    # when 字符串，指定日志切分间隔时间的单位。midnight：凌晨：12点。
    # interval 是间隔时间单位的个数，指等待多少个 when 后继续进行日志记录
    # backupCount 是保留日志文件的个数

    # 4. 创建日志信息格式
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    # 5.1 日志信息格式 设置给 控制台处理器
    st.setFormatter(formatter)
    # 5.2 日志信息格式 设置给 日志文件处理器
    fh.setFormatter(formatter)

    # 6.1 给日志器对象 添加 控制台处理器
    logger.addHandler(st)
    # 6.2 给日志器对象 添加 日志文件处理器
    logger.addHandler(fh)


if __name__ == '__main__':
    init_log_config(BASE_DIR + '/log/test.log',backupCount=5)
    logging.info("我是一个信息级别的日志")
# 7. 打印日志
# while True:
#     # logging.debug('我是一个调试级别的日志')
#     logging.info('我是一个信息级别的日志')
#     # logging.warning('我是一个警告级别的日志')
#     # logging.error('我是一个错误级别的日志')
#     # logging.critical('我是一个严重错误级别的日志')
#     time.sleep(1)