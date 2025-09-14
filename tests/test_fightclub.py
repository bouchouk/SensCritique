from system.load import fightclub
from system.clean import f_content
from system.model import f_emb, get_similar_reviews

if __name__ == "__main__":
    source_id = int(input('Enter current id '))
    print("\nCurrent content :", fightclub[fightclub['id'] == source_id]['review_content'].values[0],'\n')
    result_df = get_similar_reviews(fightclub,f_content, f_emb, source_id, 5)
    result_df.to_csv(f"results/Recommended_content_for_id_{source_id}_fightclub.csv")
    result_df.to_excel(f"results/Recommended_content_for_id_{source_id}_fightclub.xlsx")

