# 设置最低版本号

cmake_minimum_required(VERSION 3.10)

# 设置PROJECT_NAME变量

set(PROJECT_NAME demo)

# 设置工程名字

project(${PROJECT_NAME})

# 下面这段代码很重要，用于获得linux内核的GPIO设备支持

# Check Linux kernel header files for character device GPIO support

include(CheckSourceCompiles)
check_source_compiles(C "#include <linux/gpio.h>nint main(void) { GPIO_V2_LINE_FLAG_EVENT_CLOCK_REALTIME; return 0; }" HAVE_GPIO_CDEV_V2)
include(CheckSymbolExists)
check_symbol_exists(GPIO_GET_LINEEVENT_IOCTL linux/gpio.h HAVE_GPIO_CDEV_V1)
if(HAVE_GPIO_CDEV_V2)
set(GPIO_CDEV_SUPPORT 2)
elseif(HAVE_GPIO_CDEV_V1)
set(GPIO_CDEV_SUPPORT 1)
else()
set(GPIO_CDEV_SUPPORT 0)
message(WARNING "Missing character device GPIO support in Linux kernel header files. c-periphery will be built with legacy sysfs GPIO support only.")
endif()
add_definitions(-DPERIPHERY_GPIO_CDEV_SUPPORT=${GPIO_CDEV_SUPPORT})

# 查找当前目录下的所有源文件并存入DIR_SRCS变量

aux_source_directory(src DIR_SRCS)

include_directories(
./core/inc
./lib/c-periphery
./lib/lvgl/src/
./lib/lvgl/lvgl_demos/benchmark
./lib/lvgl/src/font
./lib/lvgl/lvgl_demos/music
./lib/lvgl/porting
./lib/lvgl
./lib/LCD/st7789
./lib/LCD/st7789/src
./lib/LCD/st7789/interface
./lib/LED/ws2812
./lib/LED/ws2812/interface
./lib/LED/ws2812/src
./lib/lvgl/generated/guider_customer_fonts
./lib/lvgl/generated/guider_fonts
./lib/lvgl/generated/images
./lib/lvgl/generated/
)
file(GLOB_RECURSE SOURCE_FILES "core/*.*" "lib/*.*")

# 添加一个可编译的目标到工程

add_executable(${PROJECT_NAME} ${DIR_SRCS} ${SOURCE_FILES})

# —— 手动查找 OpenH264 ——

find_library(OPENH264_LIBRARY
NAMES openh264               # 库的基础名
HINTS /lib/aarch64-linux-gnu # 搜索路径
)

if (OPENH264_LIBRARY)
message(STATUS "Found OpenH264 library: ${OPENH264_LIBRARY}")
else()
message(FATAL_ERROR "Could not find libopenh264 in /lib/aarch64-linux-gnu")
endif()

# —— 链接 OpenH264 及其依赖 ——


target_link_libraries(${PROJECT_NAME}
${OPENH264_LIBRARY}  # OpenH264
pthread              # 解码时可能用到的线程库
dl                   # 动态加载支持
)
