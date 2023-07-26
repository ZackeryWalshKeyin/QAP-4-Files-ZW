# QAP 4 One Stop Insurance Company
# Written By Zackery Walsh

# Import any required libraries
from datetime import datetime
from datetime import timedelta

# Read OSICDef.dat.
f = open("OSICDef.dat", "r+")

NextPolicy = int(f.readline())
BasicPrem = float(f.readline())
AddCarDisc = float(f.readline())
Lia = float(f.readline())
GlassCover = float(f.readline())
LoanCover = float(f.readline())
HSTRate = float(f.readline())
ProcFee = float(f.readline())

f.close()

# Main program.
dt = datetime.today()
InvoiceDate = dt
PayDate = ((dt.replace(day=1) + timedelta(days=32)).replace(day=1))

while True:
    loop = input("Enter Policy (Y/N): ").upper()
    if loop == "Y":

# Inputs -------------------------------------------------------------------------------------
        CusFirName = input("Enter First Name: ").title()
        CusLastName = input("Enter Last Name: ").title()
        Address = input("Enter Street Address: ")
        City = input("Enter City: ").title()
        Prov = input("Enter Province (XX): ").upper()
        AllowedProv = ["NL", "NS", "PEI", "NB", "QU", "ON", "MN", "SA", "AL", "BC", "NU", "NT", "YT"]

        while Prov not in AllowedProv:
            Prov = input("Enter a Valid Province (XX): ").upper()
            break

        PostCode = input("Enter Postal Code: ").upper()
        PhoneNum = input("Enter Phone Number: ")

        NumCars = int(input("Enter Number of Cars: "))
        ExtLia = input("Extra Liability (Y/N): ").upper()
        OptGlass = input("Optional Glass Coverage (Y/N): ").upper()
        OptCar = input("Optional Loaner Car (Y/N): ").upper()
        PayMeth = input("Payment Method (Full/Monthly): ").title()
        AllowedPayMeth = ["Full", "Monthly"]

        while PayMeth not in AllowedPayMeth:
            PayMeth = input("Payment must be made in 'Full' or 'Monthly': ").title()

# Calculations -----------------------------------------------------------------------------
        if ExtLia == "Y":
            LiaCost = (Lia * NumCars)
        if ExtLia == "N":
            LiaCost = 0
        if OptGlass == "Y":
            GlassCoverCost = (GlassCover * NumCars)
        if OptGlass == "N":
            GlassCoverCost = 0
        if OptCar == "Y":
            LoanCoverCost = (LoanCover * NumCars)
        if OptCar == "N":
            LoanCoverCost = 0

        TotExtCost = (float(LiaCost) + float(GlassCoverCost) + float(LoanCoverCost))

        TotInsPrem = BasicPrem + TotExtCost
        HSTCost = TotInsPrem * HSTRate
        TotCost = TotInsPrem + HSTCost

        if PayMeth == "Monthly":
            MonPayment = (TotCost + ProcFee)/8
        elif PayMeth == "Full":
            MonPayment = 0

# Formatting ---------------------------------------------------------
        LiaCostStr = "${:,.2f}".format(LiaCost)
        GlassCoverCostStr = "${:,.2f}".format(GlassCoverCost)
        LoanCoverCostStr = "${:,.2f}".format(LoanCoverCost)
        TotExtCostStr = "${:,.2f}".format(TotExtCost)
        TotInsPremStr = "${:,.2f}".format(TotInsPrem)
        HSTCostStr = "${:,.2f}".format(HSTCost)
        TotCostStr = "${:,.2f}".format(TotCost)
        MonPaymentStr = "${:,.2f}".format(MonPayment)

        if OptGlass == "Y":
            OptGlassStr = "Yes"
        elif OptGlass == "N":
            OptGlassStr = "No"

        if OptCar == "Y":
            OptCarStr = "Yes"
        elif OptCar == "N":
            OptCarStr = "No"

        InvoiceDateStr = InvoiceDate.strftime("%d/%m/%Y")
        PayDateStr = PayDate.strftime("%d/%m/%Y")

# Outputs ----------------------------------------------------------------------------
        print()
        print("----------------------------------")
        print("    One Stop Insurance Company    ")
        print("----------------------------------")
        print(f" {CusFirName} {CusLastName}")
        print(f" {Address}")
        print(f" {City} {Prov} {PostCode}")
        print(f" {PhoneNum}")
        print("----------------------------------")
        print(f" Number Of Cars Insured:      {NumCars:>3}")
        print(f" Glass Coverage:              {OptGlassStr:>3} ")
        print(f" Optional Loaner Car:         {OptCarStr:>3}")
        print("----------------------------------")
        print(f" Extra Liability:      {LiaCostStr:>10}")
        print(f" Glass Coverage:       {GlassCoverCostStr:>10}")
        print(f" Loaner Car Coverage:  {LoanCoverCostStr:>10}")
        print(f" Total Extras:         {TotExtCostStr:>10}")
        print(f" Insurance Premium:    {TotInsPremStr:>10}")
        print(f" HST:                  {HSTCostStr:>10}")
        print(f" Total:                {TotCostStr:>10}")
        print(f" Monthly Payment:      {MonPaymentStr:>10}")
        print("----------------------------------")
        print(f" Invoice Date:         {InvoiceDateStr}")
        print(f" Payment Date:         {PayDateStr}")
        print("----------------------------------")
        print()

# Saving to Policies.Dat ---------------------------------------------------
        NextPolicy += 1
        f = open("Policies.dat", "a")
        NewLine = [f"{NextPolicy}, {InvoiceDateStr}, {CusFirName}, {CusLastName}, {Address}, {City}, {Prov}, {PostCode}, {PhoneNum}, {NumCars}, {ExtLia}, {OptGlass}, {OptCar}, {PayMeth}, {TotCost}"]
        f.write(f"\n{NewLine}")
        f.close()
        print("Policy information processed and saved.")
    if loop == "N":
        break

# Saving OSICdef.Dat
f = open("OSICDef.dat", "w")
f.write(f"{NextPolicy}\n{BasicPrem}\n{AddCarDisc}\n{Lia}\n{GlassCover}\n{LoanCover}\n{HSTRate}\n{ProcFee}")
f.close()

# Housekeeping

# print(NextPolicy)
# print(BasicPrem)
# print(AddCarDisc)
# print(Lia)
# print(GlassCover)
# print(LoanerCover)
# print(HSTRate)
# print(ProcFee)
