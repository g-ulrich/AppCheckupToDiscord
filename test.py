# # from date_tools import *
# # import time
# #
# # for i in range(5):
# #     date = datetime.datetime.now()
# #     string_date = date.strftime("%Y-%m-%d %H:%M:%S")
# #     time.sleep(1)
# #     print(string_date)
# # # string_to_date = datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S")
# # # time.sleep(100)
# # # date2 = datetime.datetime.now()
# # #
# # # seconds_in_day = 24 * 60 * 60
# # # difference = date2 - date
# # # x = divmod(difference.days * seconds_in_day + difference.seconds, 60)
# # # print("Minutes {} seconds {}".format(x[0], x[1]))
# #
# #
# import datetime
#
#
# def datetime_diff(old_datetime, new_datetime, dates_are_strings=True):
#     """
#     String dates should be in this format "%Y-%m-%d %H:%M:%S"
#     """
#     seconds_in_day = 24 * 60 * 60
#     if dates_are_strings:
#         d1 = datetime.datetime.strptime(old_datetime, "%Y-%m-%d %H:%M:%S")
#         d2 = datetime.datetime.strptime(new_datetime, "%Y-%m-%d %H:%M:%S")
#     else:
#         d1, d2 = old_datetime, new_datetime
#     difference = d1 - d2
#     x = divmod(difference.days * seconds_in_day + difference.seconds, 60)
#     minutes, seconds = x[0], x[1]
#     return minutes, seconds
# #
# #
# # d = datetime.datetime.now()
# # time.sleep(2.99999)
# # c = datetime.datetime.now()
# #
# # print(datetime_diff(c, d, False))
#
# def livetrade_timestamp():
#     return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# #
# import datetime
# import database_impl as db
# import sqlite3 as sql
# # CON = sql.connect('userData/user.db')
# # x = db.get_timestamps_from_livetrade(CON, commit=False)
# # date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# # current_date = date.strftime("%Y-%m-%d %H:%M:%S")
# # current_difference = datetime_diff(current_date, x[-1])
# # print(current_difference)
# # previous_difference = datetime_diff(x[-1], x[-2])
# # print(previous_difference)
#
# print(livetrade_timestamp(), type(livetrade_timestamp()))
#
# import time
# CON = sql.connect('userData/user.db')
# # db.drop_table(CON, table="live_trade_timestamps", commit=True)
# time.sleep(10)
# while True:
#     t = livetrade_timestamp()
#     db.insert_timestamp_livetrade(CON, data=(t, ""), commit=True)
#     print(t)
#     time.sleep(70)


l = """__future__          aiohttp             html                sched
_abc                antigravity         http                secrets
_aix_support        argparse            httpcore            select
_ast                array               httpx               selectors
_asyncio            asgiref             idlelib             selenium
_bisect             ast                 idna                setuptools
_blake2             async_timeout       imaplib             shelve
_bootlocale         asynchat            imghdr              shlex
_bootsubprocess     asyncio             imp                 shutil
_bz2                asyncore            importlib           signal
_cffi_backend       atexit              inspect             site
_codecs             attr                io                  six
_codecs_cn          audioop             ipaddress           smtpd
_codecs_hk          authlib             itertools           smtplib
_codecs_iso2022     base64              itsdangerous        sndhdr
_codecs_jp          bdb                 jaraco              sniffio
_codecs_kr          binascii            jinja2              socket
_codecs_tw          binhex              json                socketserver
_collections        bisect              keyword             soupsieve
_collections_abc    bs4                 lib2to3             sqlite3
_compat_pickle      builtins            linecache           sqlparse
_compression        bz2                 locale              sre_compile
_contextvars        cProfile            logging             sre_constants
_csv                calculator          lzma                sre_parse
_ctypes             calendar            mailbox             ssl
_ctypes_test        certifi             mailcap             stat
_datetime           cffi                markupsafe          statistics
_decimal            cgi                 marshal             string
_elementtree        cgitb               math                stringprep
_functools          chardet             mimetypes           struct
_hashlib            chunk               mmap                subprocess
_heapq              click               modulefinder        sunau
_imp                cmath               more_itertools      symbol
_io                 cmd                 mouseinfo           symtable
_json               code                msilib              sys
_locale             codecs              msvcrt              sysconfig
_lsprof             codeop              multidict           tabnanny
_lzma               collections         multiprocessing     tarfile
_markupbase         colorsys            netrc               tda
_md5                compileall          nntplib             telnetlib
_msi                concurrent          nt                  tempfile
_multibytecodec     configparser        ntpath              tempora
_multiprocessing    contextlib          nturl2path          test
_opcode             contextvars         numbers             tests
_operator           copy                opcode              textwrap
_osx_support        copyreg             operator            this
_overlapped         crypt               optparse            threading
_peg_parser         cryptography        os                  time
_pickle             csv                 parser              timeit
_py_abc             ctypes              pathlib             tkinter
_pydecimal          curses              pdb                 token
_pyio               dataclasses         pickle              tokenize
_queue              datetime            pickletools         trace
_random             dateutil            pip                 traceback
_sha1               dbm                 pipes               tracemalloc
_sha256             decimal             pkg_resources       tty
_sha3               difflib             pkgutil             turtle
_sha512             dis                 platform            turtledemo
_signal             discord             plistlib            types
_sitebuiltins       discordwebhook      poplib              typing
_socket             distutils           posixpath           typing_extensions
_sqlite3            doctest             pprint              unicodedata
_sre                easy_install        profile             unittest
_ssl                email               prompt_toolkit      urllib
_stat               encodings           pstats              urllib3
_statistics         ensurepip           pty                 uu
_string             enum                py_compile          uuid
_strptime           errno               pyautogui           venv
_struct             faulthandler        pyclbr              warnings
_symtable           filecmp             pycparser           wave
_testbuffer         fileinput           pydoc               wcwidth
_testcapi           flask               pydoc_data          weakref
_testconsole        fnmatch             pyexpat             webbrowser
_testimportmultiple formatter           pygetwindow         websockets
_testinternalcapi   fractions           pymsgbox            werkzeug
_testmultiphase     ftplib              pyperclip           winreg
_thread             functools           pyrect              winsound
_threading_local    gc                  pyscreeze           wsgiref
_tkinter            genericpath         pytweening          xdrlib
_tracemalloc        getopt              pytz                xml
_uuid               getpass             queue               xmlrpc
_warnings           gettext             quopri              xxsubtype
_weakref            glob                random              yarl
_weakrefset         graphlib            re                  zipapp
_winapi             gzip                reprlib             zipfile
_xxsubinterpreters  h11                 requests            zipimport
_zoneinfo           hashlib             rfc3986             zlib
abc                 heapq               rlcompleter         zoneinfo
aifc                hmac                runpy
"""
# print(l.replace(" ", ".").split("."))
s = []
for i in l.replace(" ", ".").split("."):
    if "_" not in i and i != "" and i != "PyQt5" and i != "datetime" and i != "requests" and i != "sqlite3" and i != "pandas":
        s.append(i.replace("\n", ""))

print(s)
