from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "questions" ADD "is_active" BOOL NOT NULL DEFAULT True;
        ALTER TABLE "questions" ADD "category" VARCHAR(50);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "questions" DROP COLUMN "is_active";
        ALTER TABLE "questions" DROP COLUMN "category";"""


MODELS_STATE = (
    "eJztW1tz2jgU/isMT+nMbiclIWT3DRPSsk2gTehup52OR9iK0WAkYslNmC7/fSX5fl1Mob"
    "ETvZlzsXU+6+h8OhY/2ktiQpu+1ghZLIGzaP/Z+tHGYAn5RUb3W6sNVqtIIwQMzGxpPPOt"
    "pBTMKHOAwbjiDtgUcpEJqeGgFUMEcyl2bVsIicENEbYikYvRvQt1RizI5tDhiq9f2y7lV1"
    "x57xIG29++8UuETfgIqdCLn6uFfoegbSYCQKZwknKdrVdSNsLsUhqKx890g9juEkfGqzWb"
    "ExxaI8yE1IIYOoBBcXvmuCIeMVw/9iBEb+iRiTfEmI8J74Brs1j8W4JiECwA5aOhMkBLPO"
    "X3zpvT3un5ydnpOTeRIwklvY0XXhS75ygRGE/bG6kHDHgWEsYIN8OBIlgdsCx+F1zD0BLm"
    "g5j0TIFp+q6vg4s0tAGQZdgGggjcaIbtCV0egznB9tp/cSVQTkfXw9tp//qDiGRJ6b0tIe"
    "pPh0LTkdJ1Snp09krICc8PL3PCm7T+GU3ftcTP1pfJeCgRJJRZjnxiZDf90hZjAi4jOiYP"
    "OjBjcyyQBsBwy+jFyvzRK6VF3OX/k6Mmb3Av+RHBJpafaqjFPF4SaGIlvlvkrinBEp4E8J"
    "I4EFn4PVxLHEd8RAAbMAc3vxh98m9TP/w2wRwIpFFOOuAhrE7xqcHD40FBJgMc9G8H/Yth"
    "O5uwe4DtY3Cf5uIWX4jygROzbwaMxQNwTD0xDYWGdEhKEtpmVcvOMi0BGFgSABGGGLQP7Q"
    "UCzjqPN3mKUtJkhiZ7JUzb8qPVosKS5hkrfsQtGGJ2TlYO5sDJxy50SMHHB13PpOTT/VG3"
    "IbbYnP98c3xcgtff/ZvBu/7NEbdKMZuxr+p4umRR5U9kEOcwzCl8LJiCMZemAFlGHoefpw"
    "neGMB1dN3//CrBHa8m47eBeQzewdVES6OqqPvzpO6CNtDqJJQqFppmoVTR0NTkqBOd+uhC"
    "6secYVShrpRU3ftWB+hEqcbTYYlV8Op0xjlAFWaQcVT8IJ8fIKrzbEDfc+irRogNAS6YpH"
    "G/FLgz7ngodMMJvG90tcnkKoGuNkrD9+laG3JaK6HmRshbH7PtIYPHbBFvI7ftjiDus9Nc"
    "9YF5sj1Bd5stQbd4R9CVG4JMqS4uOql2XGKVT01k3//y/Q20QVAwigt5vKzUdoXIFPTNYa"
    "swkbM9pwT7jaSy+stNVPFtXPEt3JCXrGLN25D/gs4G38fNSU6zuxjHyKORtWBvKO5UDhJf"
    "nnevBPHP3PWbtk9SBaZkAbFm83vZiLK8cpCyKK0LTNjqs4SxKhANKhDyBVZqewcOqjiEIM"
    "LHFXIKGrTFSCa9FJzq07z6NP8En+afpiUqgc0pvgHgxSU3bHerQlu3fCwrtOK1yesKFSLu"
    "s5/6cHAUD9BPipeGFaD0gfDkmwM6rwJlxlHVW/V9+Tl+X1bb7crb7XguiNNbCP4kDuEpsY"
    "aCkLOr3x2MbDuhoaioTxQHb04lYClgx9sdGMi+rPrQZQ1Zz4gx/9HpnJz0OscnZ+fd016v"
    "e34cUuesqoxDa6O3gkYniqX6X8uLIi/JY/L+8Y+Kf21JeL2kbpBqoe0Ammqh7f3fLVF5/k"
    "nkmkmQ0uilVqQ6NSH70EHGPI9o+ZpSigUim9pQq2fEqw7WifwOHZqboMXds5hLM/tmnW53"
    "i74Ztyrsm0ld6kwIT40KIPrmzQTw1/5d6K/bybjq6SQTGaz1b6v2TYY8/ES8CVqeORacPg"
    "Gc4tviBlq1wzb7Lyyb/wAFaG3J"
)
