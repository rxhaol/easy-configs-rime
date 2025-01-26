import java.io.IOException;
import java.io.Writer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.*;
import java.util.regex.Pattern;

/**
 * @author Liang Chenghao
 *         Created on 2025/1/24
 */
public class Generate {

    private static final Pattern CSV_PATTERN = Pattern.compile("(#|0x)?[0-9a-fA-F]{6}(,.*?){2}");

    public static void main(String[] args) {
        generateRimeConfig();
    }

    public static void generateRimeConfig() {
        // 读取csv文件
        Path csv = Paths.get(getCurrentDir(), "colors.csv");
        if (!Files.exists(csv)) {
            throw new RuntimeException("找不到主题配置文件：[colors.csv]");
        }
        List<String> csvs = readFile(csv);
        if (csvs.isEmpty()) {
            throw new RuntimeException("主题配置文件内容为空");
        }
        // 写文件
        Path configPath = getRimeConfigPath();
        appendString(configPath, getHead(), false);
        appendString(configPath, formatYamlKv("patch", "", 1));
        appendString(configPath, formatYamlKv("preset_color_schemes", "", 2));
        csvs.stream().filter(c -> CSV_PATTERN.matcher(c).matches()).forEach(c -> {
            String[] values = c.split(",");
            Map<String, String> lightMap = buildThemeMap(true, values[0], values[1], values[2]);
            Map<String, String> darkMap = buildThemeMap(false, values[0], values[1], values[2]);
            writeMap(lightMap);
            writeMap(darkMap);
        });
        // 追加ending配置
        appendString(configPath, getFoot());
    }

    public static void writeMap(Map<String, String> map) {
        Path configPath = getRimeConfigPath();
        map.forEach((k, v) -> {
            if (Objects.equals("tag", k)) {
                appendString(configPath, formatYamlKv(v, "", 3));
            } else {
                appendString(configPath, formatYamlKv(k, v, 4));
            }
        });
    }

    public static List<String> readFile(String fileName) {
        Path path = Paths.get("", fileName);
        try {
            return Files.readAllLines(path);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static List<String> readFile(Path path) {
        try {
            return Files.readAllLines(path);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void appendString(Path path, String str) {
        appendString(path, str, true);
    }

    public static void appendString(Path path, String str, boolean append) {
        try {
            if (append) {
                Files.write(path, Collections.singletonList(str), StandardOpenOption.CREATE, StandardOpenOption.APPEND);
            } else {
                if (Files.exists(path)) {
                    Files.delete(path);
                }
                Files.write(path, Collections.singletonList(str), StandardOpenOption.CREATE);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void appendString(Writer writer, String str) throws IOException {
        writer.append(str).append(System.lineSeparator());
    }

    public static String getCurrentDir() {
        return System.getProperty("user.dir");
    }

    public static String formatYamlKv(String key, String value, int level) {
        if (Objects.isNull(value)) {
            return null;
        }
        if (value.contains(" ")) {
            value = "\"" + value + "\"";
        }
        if (level <= 0) {
            return String.format("%s: %s", key, value);
        }
        String blank = "  ";
        return String.format("%s: %s", blank.repeat(level - 1) + key, value);
    }

    public static Map<String, String> buildThemeMap(boolean light, String colorHex, String tag, String name) {
        if (colorHex.startsWith("#")) {
            colorHex = colorHex.substring(1);
        } else if (colorHex.startsWith("0x")) {
            colorHex = colorHex.substring(2);
        }
        colorHex = "0x" + (colorHex.toUpperCase());
        Map<String, String> map = new LinkedHashMap<>();
        if (light) {
            map.put("tag", tag);
            map.put("author", "rxhaol");
            map.put("back_color", "0xFFFFFF");
            map.put("border_color", "0xFFFFFF");
            map.put("color_format", "rgba");
            map.put("candidate_text_color", "0x454545");
            map.put("hilited_candidate_back_color", colorHex + "26");
            map.put("hilited_candidate_text_color", colorHex);
            map.put("hilited_label_color", colorHex);
            map.put("label_color", "0x8E8E8E");
            map.put("name", name);
        } else {
            map.put("tag", tag + "_dark");
            map.put("back_color", "0x000000");
            map.put("border_color", "0x000000");
            map.put("color_format", "rgba");
            map.put("candidate_text_color", "0xBABABA");
            map.put("hilited_candidate_back_color", colorHex);
            map.put("hilited_candidate_text_color", "0xFFFFFF");
            map.put("hilited_label_color", "0xFFFFFF");
            map.put("label_color", "0x717171");
            map.put("name", name + "·暗");
        }
        return map;
    }

    public static String getHead() {
        return """
                customization:
                  distribution_code_name: Weasel
                  distribution_version: 0.16.3
                  generator: "Weasel::UIStyleSettings"
                  modified_time: "Fri Jan 24 17:10:40 2025"
                  rime_version: 1.11.2
                """;
    }

    public static String getFoot() {
        return """
                  style:
                    blur: true
                    font_face: "PingFang SC:Bold"
                    font_point: 12
                    horizontal: true
                    inline_preedit: true
                    label_font_point: 10
                    layout: {border: 2, candidate_spacing: 14, hilite_padding: 4, hilite_spacing: 4, margin_x: 5, margin_y: 5, round_corner: 5, spacing: 5}
                """;
    }

    public static Path getCsvPath() {
        return Paths.get(getCurrentDir(), "colors.csv");
    }

    public static Path getRimeConfigPath() {
        return Paths.get(getCurrentDir(), "weasel.custom.yaml");
    }
}
