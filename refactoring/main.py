__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


from typing import Literal, Union


class Homeowner:
    def __init__(
        self,
        name: str,
        address: str,
        needs: list[Literal["electrician", "painter", "plumber"]],
    ):
        self.name = name
        self.address = address
        self.needs = needs


class Specialist:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Electrician(Specialist):
    profession: str = "electrician"


class Painter(Specialist):
    profession: str = "painter"


class Plumber(Specialist):
    profession: str = "plumber"


AnySpecialist = Union[Electrician, Plumber, Painter]

alice = Electrician("Alice Aliceville", 25)
bob = Painter("Bob Bobsville", 30)
craig = Plumber("Craig Craigsville", 30)

xander = Electrician("Xander Xanderston", 20)
yvette = Painter("Yvette Yvettestein", 20)
zsolt = Plumber("Zsolt Zsoltainen", 40)

specialists: list[AnySpecialist] = [alice, bob, craig, xander, yvette, zsolt]

alfred = Homeowner("Alfred Alfredson", "Alfredslane 123", ["painter", "plumber"])
bert = Homeowner("Bert Bertson", "Bertslane 231", ["plumber"])
candice = Homeowner(
    "Candice Candicedottir", "Candicelane 312", ["electrician", "painter"]
)

homeowners: list[Homeowner] = [alfred, bert, candice]

for homeowner in homeowners:
    for need in homeowner.needs:
        poss_contracts: list[AnySpecialist] = []
        for spec in specialists:
            if need == spec.profession:
                poss_contracts.append(spec)
        print(f"{homeowner.name} needs a {need}.")
        for poss in poss_contracts:
            print(f"{poss.name} can do it for {poss.price} euros.")

        min_price: int = min(x.price for x in poss_contracts)
        min_price_index: int = [spec.price for spec in poss_contracts].index(min_price)
        min_contract: AnySpecialist = poss_contracts[min_price_index]
        print(
            f"The lowest price is clearly {min_price} so {min_contract.name} should do it.\n"
        )
