import requests
import json

req_header = {
    'authority': 'rh.com',
    'path': '/rh-experience-layer-v1/graphql',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '1802',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://rh.com',
    'referer': 'https://rh.com/store-locations/stores',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'cookie': 'PF_EXP=DESKTOP; PF_DESKTOP_NEW=%5E%2Fstore-locations%7C%5E%2Fswatch%7C%5E%2Finterior-design%7C%5E%2Fcontent%2Fcategory.jsp%5C%3Fcontext%3DTrade%7C%5E%2Fcontent%2Fcategory.jsp%5C%3Fcontext%3DInteriorDesignServices%7C%5E%2Fcontent%2Fcategory.jsp%5C%3Fcontext%3DRestaurantSafety%7C%5E%2Fcontent%2Fcategory.jsp%5C%3Fcontext%3DCovidProtocol%7C%5E%2Fself-scheduler; _hjid=e5c9a7df-65ed-4a70-9ddc-e59be250263c; _svsid=508145c06f674517ccfb57a401ff30fb; _ga=GA1.2.1074896250.1605902221; rbucket=89; _gid=GA1.2.1159560181.1606143723; JSESSIONID=wQyey142qYsNnXY+we22ZpwO.e6167ed5-fd9a-398b-ad9e-33414f7ac434; DYN_USER_ID=6814049714; DYN_USER_CONFIRM=48eea7d3facc00b8605e0ffa7a2df0fb; saleContext=false; userCatalog=default; targeted_content=false; userContext="country=US,currencyCode=USA,userType=regular"; bm_mi=47352D4CC6314DB5F666A2AF50A3593E~1Zy2NFB/sFOetuoGcRexAq/Q/BZPlbO5xjx0AL1H0yMH4DakH6ajiYVTFqigN6im6XZ1grwf6k67ZLqcbapEaHwpjlJwizr4XacKK/XmDraOxcdm0H6nfhcn2pTRIRHxfbTDL9Kv2ZNXtxGmD3GRfftxlwkEGlljPz8XTIHxx+IkEPSIIKKPSroi6Qna83ml0WbvgiKciP7h2Y4xdcunla+6UfdxGspz1gvrI8OHk+9YvJtI5Bx9nZPaRXUxpKdgjGt+r4+6vq1Ga0b6UvPriHvaR9xc79J0FqBsL3IdgMs=; _gat_UA-6578887-5=1; ak_bmsc=3DDDE1D05F53988CA7B4AF8ED3C263C6D897BBC43F3100009203BC5FC7A0BE08~plrCzx7Y7OfrJcHSZRiRRemagEKyQNBkUxzn5XpuQNrXd+L/vvCr+fIVE6anF1eHq/9NufpKysKxHXG1cEkQ8VElr1KPC5pRNXtIsxY6+DLx4lOxqvZGmOWPwyp7kaRedHj1wsLadSYPDMmU2lrmKdxEElPjIC+OGBoCXnWY71vtJ1N2LcrxrY7y7M9aM/e53KhUuC3/uesaOEAz37sD/NOrxIqxz+hG1GVor3HpSvq9LnkhLoNtVvgC8/GuqeBhvB; AUTH_SESSION_ID=32a73ad5-1eb5-4c63-9cf5-85c3764e42da.keycloak-2; AUTH_SESSION_ID_LEGACY=32a73ad5-1eb5-4c63-9cf5-85c3764e42da.keycloak-2; bm_sv=9501EED869AFF1F0DE3908193143580C~hW2ckwM2ilfLzBzHPZLy1CNkG/Vb6CN7j0J7QZoY5JcNhj/fsZaXkkkJc+LefTqKiy0x7dhu8iDCyn1jeFUgV2Yv0lrHUdvZqie9y4HCKRCOndsZwTTqh1i4hiAMB/jt8ykuaw9F2Pv1tktH3XTV9w=='
}

post_data = '{"operationName":"Galleries","variables":{},"query":"query Galleries {\\n  galleries {\\n    ...GalleryInfo\\n  }\\n}\\n\\nfragment GalleryInfo on Gallery {\\n  __typename\\n  docId\\n  docType\\n  docUuid\\n  docCtime\\n  docMtime\\n  number\\n  name\\n  type\\n  replacementFacility\\n  galleryLink\\n  address {\\n    mallName\\n    streetLine1\\n    streetLine2\\n    city\\n    county\\n    state\\n    country\\n    postalCode\\n    latitude\\n    longitude\\n    timeZoneName\\n  }\\n  phoneNumber\\n  url\\n  generalEmailAddress\\n  leadsEmailAddresses\\n  description\\n  notes\\n  galleryStatus\\n  standardDailyHoursList {\\n    closeTime\\n    dayOfWeek\\n    open\\n    openTime\\n    shortNameEnUs\\n  }\\n  hours\\n  overrideHoursHash {\\n    isOpen\\n    openTime\\n    closeTime\\n    shortNameCode\\n    shortNameEnUs\\n  }\\n  collectionOfferings {\\n    offersInteriors\\n    offersModern\\n    offersContemporaryArt\\n    offersBabyAndChild\\n    offersRugShowroom\\n    offersTeen\\n    offersOutdoor\\n    offersWaterWorks\\n  }\\n  hospitalityOfferings {\\n    offers3ArtsClubCafe\\n    offers3ArtsClubWineVault\\n    offers3ArtsClubPantryBaristaBar\\n    offersRHRooftopRestaurant\\n    offersRHCourtyardCafe\\n    offersRHWineVault\\n    offersRHPantryBaristaBar\\n  }\\n  groundsFeatures {\\n    hasEuropeanGardenCourtyard\\n    hasIndoorConservatoryPark\\n    hasRooftopParkConservatory\\n    hasGroundEstateGardens\\n    hasRooftopPark\\n    hasGardenCourtyard\\n  }\\n  serviceOfferings {\\n    offersDesignAtelier\\n    offersInteriorDesign\\n  }\\n  parkingOfferings {\\n    offersOnStreet\\n    offersPrivateFreeLot\\n    offersPrivatePaidLot\\n    offersPublicFreeLot\\n    offersPublicPaidLot\\n    offersComplimentaryValet\\n    offersPaidValet\\n  }\\n  region\\n  isConciergeEnabled\\n  isRHStore\\n  isBCStore\\n  isRHCAStore\\n  isOperating\\n  heroImage\\n}\\n"}'
# post_data = '{}'
url = 'https://rh.com/rh-experience-layer-v1/graphql'

r = requests.post(url=url, data=post_data, headers=req_header, timeout=30)
rResponse = r.content
resJson = json.loads(rResponse)

print(len(resJson["data"]["galleries"]))

stores = resJson["data"]["galleries"]
if not stores:
    raise Exception("Failed to find stores")

for store in stores:
    address = store['address']

    latitude = address['latitude']
    longitude = address['longitude']

    site_id = store['docId']
    name = store['name']

    street = address['streetLine1']
    city = address['city']
    state = address['state']
    zip_code = address['postalCode']

    phone = store['phoneNumber']
