from system.load import interstellar
from system.clean import i_content
from system.model import i_emb, get_similar_reviews

if __name__ == "__main__":
    source_id = int(input('Enter current id '))
    print("\nCurrent content :", interstellar[interstellar['id'] == source_id]['review_content'].values[0],'\n')
    result_df = get_similar_reviews(interstellar, i_content, i_emb, source_id, 5)
    result_df.to_csv(f"results/Recommended_content_for_id_{source_id}_interstellar.csv")
    result_df.to_excel(f"results/Recommended_content_for_id_{source_id}_interstellar.xlsx")