from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "quotes" DROP COLUMN "is_active";
        ALTER TABLE "quotes" ALTER COLUMN "author" TYPE VARCHAR(100) USING "author"::VARCHAR(100);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "quotes" ADD "is_active" BOOL NOT NULL DEFAULT True;
        ALTER TABLE "quotes" ALTER COLUMN "author" TYPE VARCHAR(255) USING "author"::VARCHAR(255);"""


MODELS_STATE = (
    "eJztW11z2jgU/SsMT+nMbiclIWT3DRPSsk2gTehup52OR9gKaDASseQmTJf/vpL8/bmY4s"
    "ZO9GZ077V1jyWdo4v8o70iJrToa42Q5QrYy/afrR9tDFaQX6Rsv7XaYL0OLaKBgZklnWee"
    "l2wFM8psYDBuuAMWhbzJhNSw0ZohgnkrdixLNBKDOyI8D5scjO4dqDMyh2wBbW74+rXtUH"
    "7FjfcOYbD97Ru/RNiEj5AKu/i5Xup3CFpmLAFkiiDZrrPNWraNMLuUjuLxM90glrPCofN6"
    "wxYEB94IM9E6hxjagEFxe2Y7Ih/RXS93P0W366GL28VIjAnvgGOxSP47gmIQLADlvaEywb"
    "l4yu+dN6e90/OTs9Nz7iJ7ErT0tm56Ye5uoERgPG1vpR0w4HpIGEPcDBuKZHXA0vhdcAtD"
    "K5gNYjwyAabphb72L5LQ+kAWYes3hOCGI+xA6PIczAm2Nt6LK4ByOroe3k771x9EJitK7y"
    "0JUX86FJaObN0kWo/OXol2wueHO3OCm7T+GU3ftcTP1pfJeCgRJJTNbfnE0G/6pS36BBxG"
    "dEwedGBGxpjf6gPDPcMXK+ePXmpaREP+f3LU5A0eZH6EsInlpxxqkYiXBJpYie+WmWuKv4"
    "THAbwkNkRz/B5uJI4j3iOADZiBm0dGn7zb1A+/rT8G/NZwTtrgIWCn6NDg6fGkIJMJDvq3"
    "g/7FsJ2esAeA7aN/n+biFl2IsoETo28GjOUDsE09NgyFhXRIoiXwTZtWnVWyBWAwlwCINE"
    "SnPWgvELA3WbrJNRSKJjNwOahgUvqoWn3EELMyZuVgAexs7IKABHy80/WclHy4P+oWxHO2"
    "4D/fHB8X4PV3/2bwrn9zxL0SymbsmTquLU6q/IkM4gyFOYWPOUMwEtIUIIvE4/DzNKYbfb"
    "iOrvufX8W049Vk/NZ3j8A7uJpoSVSVdH+e0l3IBlpehFKlQpMqlCoZmhgcdZJTHx1IvZxT"
    "iiqwFYqqe8+rgkqUElbVCiv/1emMa4AyyiAVqPRBtj5AVOezAX3PkK8aIRYEOGeQRuMS4M"
    "54YFXoBgP40Ohqk8lVDF1tlITv07U25LJWQs2dkLs+pstDBs95TtyN3K47gmjMXmPVA+bJ"
    "9gTdXbYE3fwdQVduCFJUnU86iXJcbJVPDGQv/vL9DbSATxj5RB6lldquEClC31bLwkSO9g"
    "wK9gpJRfzLXRT5No581Ya8CsLlm7oFyah851NDGNFIYqimWKTKGs+nrLEX6cfOF+zP99HD"
    "DPV70U/C9VOyhFiz+L0sRFkW6Sc8CtmfCV99FnNWMqBBMkC+wFJ/bvgBTZEAv4Cv4OMa2T"
    "l8lY9kPErBqQ5gqAMYT3AA42kK3xLYDPL1Ac+n3OBPDUW0dZuPRUQrXpu8LsEQ0ZjD8EPl"
    "KFZQNYxSwxpQ+kD45FsAuigDZSpQ8a3abqvtttpuO/GDF+KMHoI/iUNwFrChIGTs6vcHI1"
    "1OaCgq6o+oyotTMVhy1PFux0LSL6s+cllD82ekmP/odE5Oep3jk7Pz7mmv1z0/DqRz2lSk"
    "obXRWyGjY2Spvl56UeIl/jGEd8in5AdMsaiXVA1SJbQ9QFMltIN/wxTS808i10yBlEQvsS"
    "LVqQjZhzYyFllCy7MUSiwQ+tRGWj0jXVVZJfI7tGnmBM2vnkVCmlk363S7O9TNuFdu3Uza"
    "Eod9+NQoAaLn3kwAf+1HYX/dTsZlz6CZyGCtf1u1LzJk4Sfyjcny1Fm05LGzhN4WN9DKnb"
    "A9PLFs/wM5qwkC"
)
