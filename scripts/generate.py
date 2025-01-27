import os
import re
from typing import Dict, List

# 对应 Java 中的 CSV_PATTERN
CSV_PATTERN = re.compile(r"(#|0x)?[0-9a-fA-F]{6}(,.*?){2}")


def get_current_dir() -> str:
    """
    获取当前工作目录，对应 Java 中的 getCurrentDir 方法
    :return: 当前工作目录的路径
    """
    return os.getcwd()


def read_file(file_path: str) -> List[str]:
    """
    读取文件内容，对应 Java 中的 readFile 方法
    :param file_path: 文件路径
    :return: 文件内容的行列表
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except Exception as e:
        raise RuntimeError(f"读取文件失败: {e}")


def append_string(file_path: str, content: str, append: bool = True):
    """
    向文件追加或覆盖内容，对应 Java 中的 appendString 方法
    :param file_path: 文件路径
    :param content: 要写入的内容
    :param append: 是否追加，默认为 True
    """
    mode = 'a' if append else 'w'
    try:
        with open(file_path, mode, encoding='utf-8') as file:
            file.write(content + '\n')
    except Exception as e:
        raise RuntimeError(f"写入文件失败: {e}")


def format_yaml_kv(key: str, value: str, level: int) -> str:
    """
    格式化 YAML 键值对，对应 Java 中的 formatYamlKv 方法
    :param key: 键
    :param value: 值
    :param level: 缩进级别
    :return: 格式化后的 YAML 键值对字符串
    """
    if value is None:
        return None
    if ' ' in value:
        value = f'"{value}"'
    if level <= 0:
        return f"{key}: {value}"
    blank = "  "
    return f"{blank * (level - 1)}{key}: {value}"


def build_theme_map(light: bool, color_hex: str, tag: str, name: str) -> Dict[str, str]:
    """
    构建主题映射，对应 Java 中的 buildThemeMap 方法
    :param light: 是否为亮色主题
    :param color_hex: 颜色十六进制值
    :param tag: 标签
    :param name: 名称
    :return: 主题映射字典
    """
    if color_hex.startswith("#"):
        color_hex = color_hex[1:]
    elif color_hex.startswith("0x"):
        color_hex = color_hex[2:]
    color_hex = f"0x{color_hex.upper()}"

    theme_map = {}
    if light:
        theme_map["tag"] = tag
        theme_map["author"] = "rxhaol"
        theme_map["back_color"] = "0xFFFFFF"
        theme_map["border_color"] = "0xFFFFFF"
        theme_map["color_format"] = "rgba"
        theme_map["candidate_text_color"] = "0x454545"
        theme_map["hilited_candidate_back_color"] = f"{color_hex}26"
        theme_map["hilited_candidate_text_color"] = color_hex
        theme_map["hilited_label_color"] = color_hex
        theme_map["label_color"] = "0x8E8E8E"
        theme_map["name"] = name
    else:
        theme_map["tag"] = f"{tag}_dark"
        theme_map["back_color"] = "0x000000"
        theme_map["border_color"] = "0x000000"
        theme_map["color_format"] = "rgba"
        theme_map["candidate_text_color"] = "0xBABABA"
        theme_map["hilited_candidate_back_color"] = color_hex
        theme_map["hilited_candidate_text_color"] = "0xFFFFFF"
        theme_map["hilited_label_color"] = "0xFFFFFF"
        theme_map["label_color"] = "0x717171"
        theme_map["name"] = f"{name}·暗"
    return theme_map


def write_map(theme_map: Dict[str, str]):
    """
    写入主题映射，对应 Java 中的 writeMap 方法
    :param theme_map: 主题映射字典
    """
    config_path = os.path.join(get_current_dir(), "weasel.custom.yaml")
    for k, v in theme_map.items():
        if k == "tag":
            append_string(config_path, format_yaml_kv(v, "", 3))
        else:
            append_string(config_path, format_yaml_kv(k, v, 4))


def get_head() -> str:
    """
    获取头部配置信息，对应 Java 中的 getHead 方法
    :return: 头部配置信息字符串
    """
    return """
customization:
  distribution_code_name: Weasel
  distribution_version: 0.16.3
  generator: "Weasel::UIStyleSettings"
  modified_time: "Fri Jan 24 17:10:40 2025"
  rime_version: 1.11.2
"""


def get_foot() -> str:
    """
    获取尾部配置信息，对应 Java 中的 getFoot 方法
    :return: 尾部配置信息字符串
    """
    return """
  style:
    blur: true
    font_face: "PingFang SC:Bold"
    font_point: 12
    horizontal: true
    inline_preedit: true
    label_font_point: 10
    layout: {border: 2, candidate_spacing: 14, hilite_padding: 4, hilite_spacing: 2, margin_x: 6, margin_y: 6, round_corner: 5, spacing: 5}
"""


def get_csv_path() -> str:
    """
    获取 CSV 文件路径，对应 Java 中的 getCsvPath 方法
    :return: CSV 文件路径
    """
    return os.path.join(get_current_dir(), "colors.csv")


def get_rime_config_path() -> str:
    """
    获取 Rime 配置文件路径，对应 Java 中的 getRimeConfigPath 方法
    :return: Rime 配置文件路径
    """
    return os.path.join(get_current_dir(), "weasel.custom.yaml")


def generate_rime_config():
    """
    生成 Rime 配置，对应 Java 中的 generateRimeConfig 方法
    """
    # 读取 csv 文件
    csv_path = get_csv_path()
    if not os.path.exists(csv_path):
        raise RuntimeError("找不到主题配置文件：[colors.csv]")
    csv_lines = read_file(csv_path)
    if not csv_lines:
        raise RuntimeError("主题配置文件内容为空")

    # 写文件
    config_path = get_rime_config_path()
    append_string(config_path, get_head(), False)
    append_string(config_path, format_yaml_kv("patch", "", 1))
    append_string(config_path, format_yaml_kv("preset_color_schemes", "", 2))

    for line in csv_lines:
        if CSV_PATTERN.match(line):
            values = line.split(",")
            light_map = build_theme_map(True, values[0], values[1], values[2].strip())
            dark_map = build_theme_map(False, values[0], values[1], values[2].strip())
            write_map(light_map)
            write_map(dark_map)

    # 追加 ending 配置
    append_string(config_path, get_foot())


if __name__ == "__main__":
    generate_rime_config()