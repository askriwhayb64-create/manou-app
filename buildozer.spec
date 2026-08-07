[app]

title = Manou Assistant

package.name = manouapp
package.domain = org.manou

version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3

requirements = python3,kivy,gtts,requests,urllib3,certifi,idna,charset-normalizer

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.androidx = True

[buildozer]

log_level = 2
warn_root = 1
